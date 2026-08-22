#!/usr/bin/env python3
"""Phase 6 etiologic secondary outcomes + timing subgroup/meta-regression audit.

Reads only the frozen 28-unit primary input and the audited etiologic derivation
table. It never edits scientific database values.
"""
import argparse, json, math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize, brentq
from scipy.special import roots_hermite, expit, logsumexp, gammaln
from scipy.stats import chi2

from run_phase6_meta import summarize_glmm, exact_binom_ci, fit_glmm

PRIMARY_Q=41
VALIDATION_Q=(21,31,41,61)

def timing_group(x):
    early={'EARLY_FIRST_DAY','EARLY_LT24H','EARLY_LT24H_RAW','EARLY_LT24H_PREDOMINANT',
           'EARLY_2_24H','EARLY_6_12H','VERY_EARLY_LT12H','VERY_EARLY_6H'}
    post={'POST_24H','POST24H','POST24H_PREDOMINANT_RAW'}
    if x in early: return '<24h_predominant'
    if x in post: return '>=24h_predominant'
    return 'mixed_uncertain'

def reg_loglik(params,y,n,X,q):
    beta=params[:-1]; tau=math.exp(params[-1]); x,w=roots_hermite(q); total=0.0
    for yi,ni,xi in zip(np.asarray(y,float),np.asarray(n,float),np.asarray(X,float)):
        eta0=float(xi@beta)
        logcomb=gammaln(ni+1)-gammaln(yi+1)-gammaln(ni-yi+1)
        def score(z):
            p=expit(eta0+tau*z)
            return tau*(yi-ni*p)-z
        lo,hi=-20.0,20.0
        while score(lo)<0: lo*=2
        while score(hi)>0: hi*=2
        z0=brentq(score,lo,hi)
        p0=expit(eta0+tau*z0)
        scale=1/math.sqrt(1+tau*tau*ni*p0*(1-p0))
        z=z0+math.sqrt(2)*scale*x; eta=eta0+tau*z
        logp=-np.logaddexp(0,-eta); log1mp=-np.logaddexp(0,eta)
        h=logcomb+yi*logp+(ni-yi)*log1mp-.5*z*z-.5*math.log(2*math.pi)
        total+=math.log(math.sqrt(2)*scale)+float(logsumexp(np.log(w)+h+x*x))
    return total

def design(groups):
    g=np.asarray(groups)
    return np.column_stack([np.ones(len(g)),
                            g=='<24h_predominant',
                            g=='>=24h_predominant']).astype(float)

def fit_reg(y,n,groups,q=PRIMARY_Q,start=None):
    X=design(groups); y=np.asarray(y,float); n=np.asarray(n,float)
    if start is not None:
        r=minimize(lambda z:-reg_loglik(z,y,n,X,q),start,method='L-BFGS-B',
                   bounds=[(-14,14),(-14,14),(-14,14),(-9,4)],
                   options={'ftol':1e-10,'gtol':1e-7,'maxiter':800})
        if not r.success: raise RuntimeError(str(r.message))
        return r
    p0=(y.sum()+.5)/(n.sum()+1); mu0=math.log(p0/(1-p0)); best=None
    for tau0 in (.1,.5,1,2,4,8):
        r=minimize(lambda z:-reg_loglik(z,y,n,X,q),
                   [mu0,0,0,math.log(tau0)],method='L-BFGS-B',
                   bounds=[(-14,14),(-14,14),(-14,14),(-9,4)],
                   options={'ftol':1e-11,'gtol':1e-7,'maxiter':1500})
        if best is None or r.fun<best.fun: best=r
    if not best.success: raise RuntimeError(str(best.message))
    return best

def timing_meta_regression(y,n,groups):
    full41=fit_reg(y,n,groups,41)
    vals=[]
    for q in VALIDATION_Q:
        full=full41 if q==41 else fit_reg(y,n,groups,q,start=full41.x)
        null=fit_glmm(y,n,q=q)
        lr=2*((-float(full.fun))-float(null['loglik']))
        vals.append({'q':q,'lr_chi2':float(lr),'df':2,
                     'p_value':float(chi2.sf(lr,2)),
                     'residual_tau':math.exp(float(full.x[-1])),
                     'success':bool(full.success)})
    q41=next(v for v in vals if v['q']==41)
    return {'reference':'mixed_uncertain',**q41,'quadrature_validation':vals}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--primary-input',required=True)
    ap.add_argument('--etiology-input',required=True)
    ap.add_argument('--outdir',required=True)
    a=ap.parse_args()
    primary=pd.read_csv(a.primary_input); et=pd.read_csv(a.etiology_input)
    out=Path(a.outdir); out.mkdir(parents=True,exist_ok=True)

    if len(primary)!=28 or len(et)!=28: raise RuntimeError('Expected 28 rows in both inputs')
    if set(primary.unit_id)!=set(et.unit_id): raise RuntimeError('Unit-ID mismatch')
    chk=primary[['unit_id','denominator']].merge(et[['unit_id','denominator']],on='unit_id',suffixes=('_p','_e'))
    if not np.all(chk.denominator_p.astype(int)==chk.denominator_e.astype(int)):
        raise RuntimeError('Primary/etiology denominator mismatch')

    spec={'pphn':('pphn_n','pphn_status'),
          'respiratory':('respiratory_n','respiratory_status'),
          'infection':('infection_n','infection_status'),
          'cardiac_non_target':('cardiac_non_target_n','cardiac_non_target_status')}
    results={'analysis_status':'AUTHORITATIVE_PHASE6_SECONDARY_RUN',
             'database_changed':False,'primary_membership_k':28,
             'etiology':{},'timing_subgroups':{},'timing_meta_regression':{},
             'feasibility':{
               'setting':'No formal meta-regression: only one truly out-of-hospital/homebirth primary unit and heterogeneous hospital labels.',
               'altitude':'No formal meta-regression: altitude not reported in 25/28 primary units.'},
             'guards':[
               'NOT_POINT_IDENTIFIABLE is missing for that etiologic outcome, never zero.',
               'Etiologic categories may overlap and must not be summed.',
               'Crude event/denominator ratios are descriptive only.']}
    study=[]
    for name,(num,status) in spec.items():
        s=et.loc[et[status].eq('EXACT')].copy()
        sm=summarize_glmm(s[num].astype(int),s.denominator.astype(int),profile=True,validate=True)
        results['etiology'][name]=sm
        for _,r in s.iterrows():
            y=int(r[num]); n=int(r.denominator); lo,hi=exact_binom_ci(y,n)
            study.append({'outcome':name,'unit_id':r.unit_id,'study_label':r.study_label,
                          'country':r.country,'events':y,'denominator':n,
                          'observed_proportion':y/n,'exact_ci_low':lo,'exact_ci_high':hi,
                          'timing':r.timing,'setting':r.setting,'altitude':r.altitude})
    pd.DataFrame(study).to_csv(out/'phase6_etiology_study_results.csv',index=False)

    primary=primary.copy(); primary['timing_group']=primary.timing.map(timing_group)
    rows=[]
    for group in ('<24h_predominant','>=24h_predominant','mixed_uncertain'):
        s=primary.loc[primary.timing_group.eq(group)]
        for ep in ('strict','expanded'):
            sm=summarize_glmm(s[ep],s.denominator,profile=True,validate=False)
            results['timing_subgroups'][f'{group}:{ep}']=sm
            rows.append({'dimension':'timing','subgroup':group,'endpoint':ep,'k':sm['k'],
                         'events':sm['events'],'denominator':sm['denominator'],
                         'crude_ratio':sm['events']/sm['denominator'],
                         'pooled_probability':sm['pooled_median_study_probability'],
                         'ci_low':sm['pooled_median_study_probability_ci95'][0],
                         'ci_high':sm['pooled_median_study_probability_ci95'][1],
                         'marginal_probability':sm['marginal_mean_probability'],
                         'tau':sm['tau'],
                         'prediction_low':sm['prediction_interval_probability'][0],
                         'prediction_high':sm['prediction_interval_probability'][1]})
    pd.DataFrame(rows).to_csv(out/'phase6_subgroup_results.csv',index=False)

    for ep in ('strict','expanded'):
        results['timing_meta_regression'][ep]=timing_meta_regression(
            primary[ep],primary.denominator,primary.timing_group)

    (out/'phase6_secondary_results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    print('Phase 6 secondary analysis complete:',out)

if __name__=='__main__':
    main()
