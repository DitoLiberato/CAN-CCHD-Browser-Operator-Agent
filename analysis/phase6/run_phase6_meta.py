#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize, minimize_scalar, brentq
from scipy.special import roots_hermitenorm, roots_hermite, expit, logsumexp, gammaln, betaln
from scipy.stats import beta, chi2, t

SQRT2PI = math.sqrt(2*math.pi)


def exact_binom_ci(y, n, alpha=0.05):
    if n <= 0:
        return (math.nan, math.nan)
    lo = 0.0 if y == 0 else beta.ppf(alpha/2, y, n-y+1)
    hi = 1.0 if y == n else beta.ppf(1-alpha/2, y+1, n-y)
    return float(lo), float(hi)


def glmm_loglik(params, y, n, q=21):
    """Adaptive Gauss-Hermite quadrature for binomial-logistic-normal random effects."""
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


def fit_glmm(y, n, q=21):
    y = np.asarray(y, float); n = np.asarray(n, float)
    p0 = (y.sum()+0.5)/(n.sum()+1.0)
    mu0 = math.log(p0/(1-p0))
    best = None
    for tau0 in (0.1, 0.3, 0.7, 1.5, 3.0, 5.0):
        r = minimize(lambda z: -glmm_loglik(z, y, n, q),
                     x0=[mu0, math.log(tau0)], method='L-BFGS-B',
                     bounds=[(-14,14),(-9,4)])
        if best is None or r.fun < best.fun:
            best = r
    if not best.success:
        raise RuntimeError(f'GLMM failed: {best.message}')
    mu, log_tau = map(float, best.x)
    tau = math.exp(log_tau)
    return {'fit': best, 'mu': mu, 'tau': tau, 'tau2': tau*tau,
            'loglik': -float(best.fun), 'quadrature_points': q}


def profile_mu_ci(y, n, fit, alpha=0.05, q=21):
    y=np.asarray(y,float); n=np.asarray(n,float)
    llmax=fit['loglik']; muhat=fit['mu']
    cutoff=float(chi2.ppf(1-alpha,1))
    def prof_ll(mu):
        r=minimize_scalar(lambda lt: -glmm_loglik([mu, lt], y, n, q),
                          bounds=(-9,4), method='bounded', options={'xatol':1e-6})
        return -float(r.fun)
    def g(mu):
        return 2*(llmax-prof_ll(mu))-cutoff
    step=.2; lo_a=muhat-step
    while g(lo_a)<0 and lo_a>-14:
        step*=1.5; lo_a=muhat-step
    lo=brentq(g, lo_a, muhat)
    step=.2; hi_b=muhat+step
    while g(hi_b)<0 and hi_b<14:
        step*=1.5; hi_b=muhat+step
    hi=brentq(g, muhat, hi_b)
    return float(lo), float(hi)


def marginal_mean(mu, tau, q=80):
    x,w=roots_hermitenorm(q)
    return float(np.sum(w*expit(mu+tau*x))/SQRT2PI)


def summarize_glmm(y,n,q=21, profile=True):
    fit=fit_glmm(y,n,q)
    if profile:
        try:
            lo,hi=profile_mu_ci(y,n,fit,q=q)
        except Exception:
            lo,hi=(math.nan, math.nan)
    else:
        lo,hi=(math.nan, math.nan)
    mu,tau=fit['mu'],fit['tau']
    return {
        'k': int(len(y)), 'events': int(np.sum(y)), 'denominator': int(np.sum(n)),
        'mu_logit': mu, 'tau': tau, 'tau2': fit['tau2'], 'loglik': fit['loglik'],
        'quadrature_points': fit['quadrature_points'],
        'pooled_median_study_probability': float(expit(mu)),
        'pooled_median_study_probability_ci95': [None if math.isnan(lo) else float(expit(lo)), None if math.isnan(hi) else float(expit(hi))],
        'marginal_mean_probability': marginal_mean(mu,tau),
        'prediction_interval_probability': [float(expit(mu-1.96*tau)), float(expit(mu+1.96*tau))]
    }


def fit_beta_binomial(y,n):
    y=np.asarray(y,float); n=np.asarray(n,float)
    p0=(y.sum()+0.5)/(n.sum()+1)
    eta0=math.log(p0/(1-p0))
    def nll(z):
        eta, logphi=z
        m=expit(eta); phi=math.exp(logphi)
        a=m*phi; b=(1-m)*phi
        ll=(gammaln(n+1)-gammaln(y+1)-gammaln(n-y+1)+
            betaln(y+a,n-y+b)-betaln(a,b)).sum()
        return -float(ll)
    best=None
    for phi0 in (0.5,1,2,5,20,100):
        r=minimize(nll,[eta0,math.log(phi0)],method='L-BFGS-B',bounds=[(-14,14),(-8,12)])
        if best is None or r.fun<best.fun: best=r
    eta,logphi=map(float,best.x); m=float(expit(eta)); phi=math.exp(logphi)
    return {'converged':bool(best.success),'mean_probability':m,'precision_phi':phi,
            'intraclass_rho':1/(phi+1),'loglik':-float(best.fun)}


def conventional_logit_reml_hk(y,n):
    y=np.asarray(y,float); n=np.asarray(n,float)
    # Jeffreys empirical-logit correction to every study, sensitivity only
    yy=y+0.5; nn=n+1.0
    p=yy/nn
    z=np.log(p/(1-p))
    v=1/yy + 1/(nn-yy)
    def reml_nll(log_tau2):
        tau2=math.exp(log_tau2)
        w=1/(v+tau2); sw=w.sum(); mu=(w*z).sum()/sw
        q=(w*(z-mu)**2).sum()
        return 0.5*(np.log(v+tau2).sum()+math.log(sw)+q)
    r=minimize_scalar(reml_nll,bounds=(-16,8),method='bounded')
    tau2=max(0.0,math.exp(float(r.x)))
    w=1/(v+tau2); sw=w.sum(); mu=float((w*z).sum()/sw)
    q=float((w*(z-mu)**2).sum())
    se_hk=math.sqrt((q/(len(z)-1))/sw)
    crit=float(t.ppf(.975,len(z)-1))
    ci=(mu-crit*se_hk,mu+crit*se_hk)
    wf=1/v; muf=(wf*z).sum()/wf.sum(); Q=float((wf*(z-muf)**2).sum()); df=len(z)-1
    I2=max(0.0,(Q-df)/Q)*100 if Q>0 else 0.0
    return {'method':'logit_REML_HartungKnapp_Jeffreys_0.5_all_studies','tau2':tau2,
            'pooled_probability':float(expit(mu)), 'ci95':[float(expit(ci[0])),float(expit(ci[1]))],
            'I2_percent':float(I2), 'Q':Q, 'df':int(df)}


def aggregate_r125(df):
    mask=df['program_cluster'].fillna('').eq('R125_SIBEN_2020')
    part=df.loc[mask]
    if len(part)!=2:
        raise RuntimeError(f'Expected 2 R125 primary units, found {len(part)}')
    agg={c:None for c in df.columns}
    agg.update({'unit_id':'U_R125_SIBEN_AGGREGATED_SENSITIVITY','study_label':'R125 SIBEN aggregated report cluster',
                'country':'MULTISITE','program_cluster':'R125_SIBEN_2020_AGG'})
    for c in ['final_failed','target','denominator','strict','can_u','expanded','noncan','healthy','unknown']:
        agg[c]=int(part[c].sum())
    out=pd.concat([df.loc[~mask],pd.DataFrame([agg])],ignore_index=True)
    return out


def endpoint_results(df, endpoint):
    y=df[endpoint].astype(int).to_numpy(); n=df['denominator'].astype(int).to_numpy()
    return summarize_glmm(y,n), fit_beta_binomial(y,n), conventional_logit_reml_hk(y,n)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',required=True)
    ap.add_argument('--preamendment-input')
    ap.add_argument('--outdir',required=True)
    ap.add_argument('--run-loo', action='store_true')
    args=ap.parse_args()
    out=Path(args.outdir); out.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(args.input)
    required=['unit_id','denominator','strict','can_u','expanded','noncan','healthy','unknown']
    miss=[c for c in required if c not in df.columns]
    if miss: raise RuntimeError(f'Missing columns {miss}')
    terminal=df[['strict','can_u','noncan','healthy','unknown']].sum(axis=1)
    if not np.all(terminal.astype(int)==df.denominator.astype(int)):
        raise RuntimeError('Terminal-state arithmetic does not equal denominator for all rows')
    if not np.all((df.strict+df.can_u).astype(int)==df.expanded.astype(int)):
        raise RuntimeError('Expanded != Strict + CAN-U')

    results={'primary_strict':{},'secondary_expanded':{},'sensitivities':{},'descriptive':{}}
    for endpoint,key in [('strict','primary_strict'),('expanded','secondary_expanded')]:
        glmm,bb,conv=endpoint_results(df,endpoint)
        results[key]={'glmm':glmm,'beta_binomial':bb,'conventional_two_stage':conv}

    r125=aggregate_r125(df)
    for endpoint in ('strict','expanded'):
        results['sensitivities'][f'r125_aggregated_{endpoint}']=summarize_glmm(
            r125[endpoint].astype(int).to_numpy(),r125.denominator.astype(int).to_numpy(), profile=False)

    if args.run_loo:
        loo=[]
        for endpoint in ('strict','expanded'):
            for i,row in df.iterrows():
                d=df.drop(i)
                s=summarize_glmm(d[endpoint].astype(int).to_numpy(),d.denominator.astype(int).to_numpy(), profile=False)
                loo.append({'endpoint':endpoint,'omitted_unit':row.unit_id,
                            'pooled_probability':s['pooled_median_study_probability'],'tau':s['tau']})
        pd.DataFrame(loo).to_csv(out/'phase6_leave_one_out.csv',index=False)

    if args.preamendment_input:
        pre=pd.read_csv(args.preamendment_input)
        for endpoint in ('strict','expanded'):
            results['sensitivities'][f'preamendment_tga_{endpoint}']=summarize_glmm(
                pre[endpoint].astype(int).to_numpy(),pre.denominator.astype(int).to_numpy(), profile=False)

    results['descriptive']={
        'k':int(len(df)), 'denominator_sum':int(df.denominator.sum()),
        'strict_sum':int(df.strict.sum()), 'expanded_sum':int(df.expanded.sum()),
        'strict_zero_event_units':int((df.strict==0).sum()),
        'strict_all_event_units':int((df.strict==df.denominator).sum()),
        'expanded_zero_event_units':int((df.expanded==0).sum()),
        'expanded_all_event_units':int((df.expanded==df.denominator).sum()),
        'minimum_denominator':int(df.denominator.min()), 'median_denominator':float(df.denominator.median()),
        'maximum_denominator':int(df.denominator.max())
    }

    stud=[]
    for _,r in df.iterrows():
        for ep in ('strict','expanded'):
            y=int(r[ep]); n=int(r.denominator); lo,hi=exact_binom_ci(y,n)
            stud.append({'unit_id':r.unit_id,'study_label':r.study_label,'endpoint':ep,
                         'events':y,'denominator':n,'observed_proportion':y/n,
                         'exact_ci_low':lo,'exact_ci_high':hi})
    pd.DataFrame(stud).to_csv(out/'phase6_study_results.csv',index=False)
    (out/'phase6_primary_results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
    print(json.dumps(results,indent=2))

if __name__=='__main__': main()
