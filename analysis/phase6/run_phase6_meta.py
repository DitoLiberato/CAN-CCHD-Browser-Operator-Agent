#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize, minimize_scalar, brentq
from scipy.special import roots_hermite, roots_hermitenorm, expit, logsumexp, gammaln, betaln
from scipy.stats import beta, chi2, t

SQRT2PI = math.sqrt(2*math.pi)
PRIMARY_Q = 41
VALIDATION_Q = (21, 31, 41, 61)


def exact_binom_ci(y, n, alpha=0.05):
    if n <= 0:
        return (math.nan, math.nan)
    lo = 0.0 if y == 0 else beta.ppf(alpha/2, y, n-y+1)
    hi = 1.0 if y == n else beta.ppf(1-alpha/2, y+1, n-y)
    return float(lo), float(hi)


def glmm_loglik(params, y, n, q=PRIMARY_Q):
    mu, log_tau = params
    tau = math.exp(log_tau)
    x, w = roots_hermite(q)
    total = 0.0
    for yi, ni in zip(y, n):
        logcomb = gammaln(ni+1)-gammaln(yi+1)-gammaln(ni-yi+1)
        def score_z(z):
            p = expit(mu + tau*z)
            return tau*(yi-ni*p)-z
        lo, hi = -20.0, 20.0
        while score_z(lo) < 0: lo *= 2
        while score_z(hi) > 0: hi *= 2
        z0 = brentq(score_z, lo, hi)
        p0 = expit(mu + tau*z0)
        scale = 1.0 / math.sqrt(1.0 + tau*tau*ni*p0*(1-p0))
        z = z0 + math.sqrt(2.0)*scale*x
        eta = mu + tau*z
        logp = -np.logaddexp(0, -eta)
        log1mp = -np.logaddexp(0, eta)
        h = logcomb + yi*logp + (ni-yi)*log1mp - 0.5*z*z - 0.5*math.log(2*math.pi)
        total += math.log(math.sqrt(2.0)*scale) + float(logsumexp(np.log(w)+h+x*x))
    return total


def fit_glmm(y, n, q=PRIMARY_Q, starts=(0.05,0.1,0.3,0.7,1.5,3.0,5.0,10.0)):
    y = np.asarray(y, float); n = np.asarray(n, float)
    p0 = (y.sum()+0.5)/(n.sum()+1.0)
    mu0 = math.log(p0/(1-p0))
    best = None; runs=[]
    for tau0 in starts:
        r = minimize(lambda z: -glmm_loglik(z, y, n, q),
                     x0=[mu0, math.log(tau0)], method='L-BFGS-B',
                     bounds=[(-14,14),(-9,4)],
                     options={'ftol':1e-12,'gtol':1e-8,'maxiter':1000})
        runs.append({'tau_start':tau0,'success':bool(r.success),'nll':float(r.fun),
                     'mu':float(r.x[0]),'log_tau':float(r.x[1])})
        if best is None or r.fun < best.fun: best = r
    if not best.success:
        raise RuntimeError(f'GLMM failed: {best.message}')
    mu, log_tau = map(float, best.x); tau = math.exp(log_tau)
    return {'fit':best,'mu':mu,'tau':tau,'tau2':tau*tau,'loglik':-float(best.fun),
            'quadrature_points':q,'optimizer_runs':runs}


def fit_glmm_warm(y,n,x0,q=21):
    r=minimize(lambda z:-glmm_loglik(z,np.asarray(y,float),np.asarray(n,float),q),x0=x0,
               method='L-BFGS-B',bounds=[(-14,14),(-9,4)],
               options={'ftol':1e-10,'gtol':1e-7,'maxiter':300})
    if not r.success: raise RuntimeError(str(r.message))
    return float(r.x[0]), math.exp(float(r.x[1]))


def profile_mu_ci(y, n, fit, alpha=0.05, q=PRIMARY_Q):
    y=np.asarray(y,float); n=np.asarray(n,float); llmax=fit['loglik']; muhat=fit['mu']
    cutoff=float(chi2.ppf(1-alpha,1))
    def prof_ll(mu):
        r=minimize_scalar(lambda lt: -glmm_loglik([mu, lt], y, n, q),
                          bounds=(-9,4), method='bounded', options={'xatol':1e-7})
        return -float(r.fun)
    def g(mu): return 2*(llmax-prof_ll(mu))-cutoff
    step=.2; a=muhat-step
    while g(a)<0 and a>-14: step*=1.5; a=muhat-step
    lo=brentq(g,a,muhat)
    step=.2; b=muhat+step
    while g(b)<0 and b<14: step*=1.5; b=muhat+step
    hi=brentq(g,muhat,b)
    return float(lo),float(hi)


def marginal_mean(mu,tau,q=100):
    x,w=roots_hermitenorm(q)
    return float(np.sum(w*expit(mu+tau*x))/SQRT2PI)


def num_hessian(fun,x,h=1e-4):
    x=np.asarray(x,float); m=len(x); H=np.zeros((m,m)); f0=fun(x)
    for i in range(m):
        ei=np.zeros(m); ei[i]=h
        H[i,i]=(fun(x+ei)-2*f0+fun(x-ei))/h**2
        for j in range(i+1,m):
            ej=np.zeros(m); ej[j]=h
            H[i,j]=H[j,i]=(fun(x+ei+ej)-fun(x+ei-ej)-fun(x-ei+ej)+fun(x-ei-ej))/(4*h*h)
    return H


def summarize_glmm(y,n,q=PRIMARY_Q,profile=True,validate=False):
    y=np.asarray(y,float); n=np.asarray(n,float); fit=fit_glmm(y,n,q)
    lo,hi=(profile_mu_ci(y,n,fit,q=q) if profile else (math.nan,math.nan))
    mu,tau=fit['mu'],fit['tau']; x=np.array([mu,math.log(tau)])
    H=num_hessian(lambda z:-glmm_loglik(z,y,n,q),x)
    eig=np.linalg.eigvalsh(H)
    out={'k':int(len(y)),'events':int(y.sum()),'denominator':int(n.sum()),
         'mu_logit':mu,'tau':tau,'tau2':tau*tau,'loglik':fit['loglik'],'quadrature_points':q,
         'pooled_median_study_probability':float(expit(mu)),
         'pooled_median_study_probability_ci95':[None if math.isnan(lo) else float(expit(lo)),None if math.isnan(hi) else float(expit(hi))],
         'marginal_mean_probability':marginal_mean(mu,tau),
         'prediction_interval_probability':[float(expit(mu-1.96*tau)),float(expit(mu+1.96*tau))],
         'optimizer_all_starts_converged':all(r['success'] for r in fit['optimizer_runs']),
         'optimizer_runs':fit['optimizer_runs'],
         'hessian_eigenvalues':[float(v) for v in eig],
         'hessian_positive_definite':bool(np.all(eig>0)),
         'hessian_condition_number':float(np.linalg.cond(H))}
    if validate:
        vals=[]
        for qq in VALIDATION_Q:
            ff=fit_glmm(y,n,q=qq)
            vals.append({'q':qq,'pooled_probability':float(expit(ff['mu'])),'tau':ff['tau'],'loglik':ff['loglik']})
        out['quadrature_validation']=vals
    return out


def fit_beta_binomial(y,n):
    y=np.asarray(y,float); n=np.asarray(n,float); p0=(y.sum()+.5)/(n.sum()+1)
    eta0=math.log(p0/(1-p0))
    def nll(z):
        eta,logphi=z; m=expit(eta); phi=math.exp(logphi); a=m*phi; b=(1-m)*phi
        ll=(gammaln(n+1)-gammaln(y+1)-gammaln(n-y+1)+betaln(y+a,n-y+b)-betaln(a,b)).sum()
        return -float(ll)
    best=None
    for phi0 in (.2,.5,1,2,5,20,100):
        r=minimize(nll,[eta0,math.log(phi0)],method='L-BFGS-B',bounds=[(-14,14),(-8,12)])
        if best is None or r.fun<best.fun: best=r
    eta,logphi=map(float,best.x); m=float(expit(eta)); phi=math.exp(logphi)
    return {'converged':bool(best.success),'mean_probability':m,'precision_phi':phi,
            'intraclass_rho':1/(phi+1),'loglik':-float(best.fun)}


def conventional_logit_reml_hk(y,n):
    y=np.asarray(y,float); n=np.asarray(n,float); yy=y+.5; nn=n+1.0
    p=yy/nn; z=np.log(p/(1-p)); v=1/yy+1/(nn-yy)
    def reml(logtau2):
        tau2=math.exp(logtau2); w=1/(v+tau2); sw=w.sum(); mu=(w*z).sum()/sw
        return .5*(np.log(v+tau2).sum()+math.log(sw)+(w*(z-mu)**2).sum())
    r=minimize_scalar(reml,bounds=(-16,8),method='bounded'); tau2=math.exp(float(r.x))
    w=1/(v+tau2); sw=w.sum(); mu=float((w*z).sum()/sw); q=float((w*(z-mu)**2).sum())
    se=math.sqrt((q/(len(z)-1))/sw); crit=float(t.ppf(.975,len(z)-1))
    wf=1/v; muf=(wf*z).sum()/wf.sum(); Q=float((wf*(z-muf)**2).sum()); df=len(z)-1
    I2=max(0.0,(Q-df)/Q)*100 if Q>0 else 0.0
    return {'method':'logit_REML_HartungKnapp_Jeffreys_0.5_all_studies','tau2':tau2,'tau':math.sqrt(tau2),
            'pooled_probability':float(expit(mu)),'ci95':[float(expit(mu-crit*se)),float(expit(mu+crit*se))],
            'I2_percent':float(I2),'Q':Q,'df':int(df)}


def aggregate_r125(df):
    mask=df['program_cluster'].fillna('').eq('R125_SIBEN_2020'); part=df.loc[mask]
    if len(part)!=2: raise RuntimeError(f'Expected 2 R125 units, found {len(part)}')
    agg={c:None for c in df.columns}; agg.update({'unit_id':'U_R125_SIBEN_AGGREGATED_SENSITIVITY',
        'study_label':'R125 SIBEN aggregated report cluster','country':'MULTISITE','program_cluster':'R125_SIBEN_2020_AGG'})
    for c in ['final_failed','target','denominator','strict','can_u','expanded','noncan','healthy','unknown']:
        agg[c]=int(part[c].sum())
    return pd.concat([df.loc[~mask],pd.DataFrame([agg])],ignore_index=True)


def timing_group(x):
    early={'EARLY_FIRST_DAY','EARLY_LT24H','EARLY_LT24H_RAW','EARLY_LT24H_PREDOMINANT','EARLY_2_24H','EARLY_6_12H','VERY_EARLY_LT12H','VERY_EARLY_6H'}
    post={'POST_24H','POST24H','POST24H_PREDOMINANT_RAW'}
    if x in early: return '<24h_predominant'
    if x in post: return '>=24h_predominant'
    return 'mixed_or_uncertain'


def forest_svg(df,endpoint,outfile,title):
    rowh=24; left=340; plotw=520; right=180; top=55; bottom=45
    h=top+len(df)*rowh+bottom; width=left+plotw+right
    e=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{h}" viewBox="0 0 {width} {h}">',
       '<style>text{font-family:Arial,sans-serif;fill:#111}.lab{font-size:12px}.small{font-size:11px}.title{font-size:18px;font-weight:700}.axis{stroke:#bbb;stroke-width:1}.ci{stroke:#333;stroke-width:1.4}.pt{fill:#111}</style>',
       f'<text x="10" y="26" class="title">{title}</text>']
    for p in [0,.25,.5,.75,1]:
        x=left+p*plotw
        e.append(f'<line x1="{x}" y1="{top-10}" x2="{x}" y2="{h-bottom}" class="axis"/>')
        e.append(f'<text x="{x}" y="{h-18}" text-anchor="middle" class="small">{int(p*100)}%</text>')
    for idx,(_,r) in enumerate(df.iloc[::-1].iterrows()):
        yc=top+idx*rowh; ev=int(r[endpoint]); n=int(r.denominator); prop=ev/n; lo,hi=exact_binom_ci(ev,n)
        label=str(r.study_label).replace('&','&amp;')
        e += [f'<text x="10" y="{yc+4}" class="lab">{label}</text>',
              f'<line x1="{left+lo*plotw:.2f}" y1="{yc}" x2="{left+hi*plotw:.2f}" y2="{yc}" class="ci"/>',
              f'<circle cx="{left+prop*plotw:.2f}" cy="{yc}" r="3.3" class="pt"/>',
              f'<text x="{left+plotw+15}" y="{yc+4}" class="small">{ev}/{n} ({prop*100:.1f}%)</text>']
    e.append('</svg>'); Path(outfile).write_text('\n'.join(e),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--preamendment-input',required=True); ap.add_argument('--outdir',required=True)
    args=ap.parse_args(); out=Path(args.outdir); out.mkdir(parents=True,exist_ok=True); (out.parent/'figures').mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(args.input); pre=pd.read_csv(args.preamendment_input)
    terminal=df[['strict','can_u','noncan','healthy','unknown']].sum(axis=1)
    if not np.all(terminal.astype(int)==df.denominator.astype(int)): raise RuntimeError('Terminal arithmetic fail')
    if not np.all((df.strict+df.can_u).astype(int)==df.expanded.astype(int)): raise RuntimeError('Expanded arithmetic fail')

    results={'analysis_status':'AUTHORITATIVE_PHASE6_RUN','primary_strict':{},'secondary_expanded':{},'sensitivities':{},'descriptive':{}}
    sensitivity_rows=[]
    for ep,key in [('strict','primary_strict'),('expanded','secondary_expanded')]:
        glmm=summarize_glmm(df[ep],df.denominator,profile=True,validate=True)
        bb=fit_beta_binomial(df[ep],df.denominator); conv=conventional_logit_reml_hk(df[ep],df.denominator)
        results[key]={'glmm':glmm,'beta_binomial':bb,'conventional_two_stage':conv}
        sensitivity_rows.append({'analysis':'beta_binomial','endpoint':ep,'k':len(df),'estimate':bb['mean_probability'],'ci_low':None,'ci_high':None,'tau':None,'notes':'Marginal mean under beta mixing distribution'})
        sensitivity_rows.append({'analysis':'conventional_two_stage','endpoint':ep,'k':len(df),'estimate':conv['pooled_probability'],'ci_low':conv['ci95'][0],'ci_high':conv['ci95'][1],'tau':conv['tau'],'notes':f"REML/HK; I2={conv['I2_percent']:.2f}%"})

    r125=aggregate_r125(df)
    for ep in ('strict','expanded'):
        s=summarize_glmm(r125[ep],r125.denominator,profile=True)
        results['sensitivities'][f'r125_aggregated_{ep}']=s
        sensitivity_rows.append({'analysis':'R125_report_cluster_aggregated','endpoint':ep,'k':len(r125),'estimate':s['pooled_median_study_probability'],'ci_low':s['pooled_median_study_probability_ci95'][0],'ci_high':s['pooled_median_study_probability_ci95'][1],'tau':s['tau'],'notes':'Barranquilla+Rosario replaced by one 39-denominator report-cluster row'})

    for ep in ('strict','expanded'):
        s=summarize_glmm(pre[ep],pre.denominator,profile=True)
        results['sensitivities'][f'historical_preamendment_prererun_{ep}']=s
        sensitivity_rows.append({'analysis':'historical_preamendment_prererun','endpoint':ep,'k':len(pre),'estimate':s['pooled_median_study_probability'],'ci_low':s['pooled_median_study_probability_ci95'][0],'ci_high':s['pooled_median_study_probability_ci95'][1],'tau':s['tau'],'notes':'Corrected 26-unit historical Snapshot R/S framework; not a pure one-variable d-TGA causal contrast'})

    loo=[]
    for ep,key in [('strict','primary_strict'),('expanded','secondary_expanded')]:
        full=results[key]['glmm']; x0=[full['mu_logit'],math.log(full['tau'])]
        for i,row in df.iterrows():
            d=df.drop(i); mu,tau=fit_glmm_warm(d[ep],d.denominator,x0,q=21)
            loo.append({'endpoint':ep,'omitted_unit':row.unit_id,'study_label':row.study_label,'pooled_probability':float(expit(mu)),'tau':tau})
    loo_df=pd.DataFrame(loo); loo_df.to_csv(out/'phase6_leave_one_out.csv',index=False)
    results['sensitivities']['leave_one_out_summary']={}
    for ep in ('strict','expanded'):
        z=loo_df[loo_df.endpoint==ep]
        results['sensitivities']['leave_one_out_summary'][ep]={'pooled_probability_range':[float(z.pooled_probability.min()),float(z.pooled_probability.max())],
            'tau_range':[float(z.tau.min()),float(z.tau.max())],
            'min_pooled_omission':str(z.loc[z.pooled_probability.idxmin(),'omitted_unit']),
            'max_pooled_omission':str(z.loc[z.pooled_probability.idxmax(),'omitted_unit'])}

    tdf=df.copy(); tdf['timing_group']=tdf.timing.map(timing_group)
    # Timing groups are retained for later prespecified subgroup work. No subgroup GLMM is forced here;
    # the >=24 h Strict subset is numerically sparse/boundary-heavy and requires a separate stability audit.

    stud=[]
    for _,r in df.iterrows():
        for ep in ('strict','expanded'):
            y=int(r[ep]); n=int(r.denominator); lo,hi=exact_binom_ci(y,n)
            stud.append({'unit_id':r.unit_id,'study_label':r.study_label,'endpoint':ep,'events':y,'denominator':n,'observed_proportion':y/n,'exact_ci_low':lo,'exact_ci_high':hi})
    pd.DataFrame(stud).to_csv(out/'phase6_study_results.csv',index=False)
    pd.DataFrame(sensitivity_rows).to_csv(out/'phase6_sensitivity_results.csv',index=False)
    results['descriptive']={'k':int(len(df)),'denominator_sum':int(df.denominator.sum()),'strict_sum':int(df.strict.sum()),'expanded_sum':int(df.expanded.sum()),
        'crude_strict_ratio':float(df.strict.sum()/df.denominator.sum()),'crude_expanded_ratio':float(df.expanded.sum()/df.denominator.sum()),
        'strict_zero_event_units':int((df.strict==0).sum()),'strict_all_event_units':int((df.strict==df.denominator).sum()),
        'expanded_zero_event_units':int((df.expanded==0).sum()),'expanded_all_event_units':int((df.expanded==df.denominator).sum()),
        'minimum_denominator':int(df.denominator.min()),'median_denominator':float(df.denominator.median()),'maximum_denominator':int(df.denominator.max()),
        'timing_group_counts':{k:int(v) for k,v in tdf.timing_group.value_counts().items()}}
    (out/'phase6_primary_results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    forest_svg(df,'strict',out.parent/'figures'/'forest_strict.svg','Strict CAN-CCHD — study proportions')
    forest_svg(df,'expanded',out.parent/'figures'/'forest_expanded.svg','Expanded CAN-CCHD — study proportions')
    print(json.dumps({'strict':results['primary_strict']['glmm'],'expanded':results['secondary_expanded']['glmm'],'descriptive':results['descriptive'],'loo':results['sensitivities']['leave_one_out_summary']},indent=2))

if __name__=='__main__': main()
