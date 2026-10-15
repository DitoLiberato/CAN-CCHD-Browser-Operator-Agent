#!/usr/bin/env python3
"""Run 46 synthetic project-integrity scenarios; never authenticate scientific approval.

Defaults to ../skills/research-assistant-pipeline relative to this script and retains
fixtures in a newly owned temporary directory. An explicit --output must be absent
or empty. No existing output is deleted or overwritten. The prose handoff case
records a documented manual-review boundary and expects STRUCTURAL_PASS.
"""
import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skill', type=Path,
                        default=Path(__file__).resolve().parent.parent / 'skills' / 'research-assistant-pipeline',
                        help='Skill distribution to test (must contain valid manifest and scripts).')
    parser.add_argument('--output', type=Path,
                        help='Absent or empty output directory; default creates a retained temporary directory.')
    args = parser.parse_args()
    SKILL = args.skill.expanduser().resolve()
    for relative in ('scripts/bootstrap_project.py', 'scripts/validate_project.py', 'manifest.json'):
        if not (SKILL / relative).is_file():
            parser.error(f'Missing skill file: {SKILL / relative}')
    if args.output is None:
        ROOT = Path(tempfile.mkdtemp(prefix='research-pipeline-integrity-')).resolve()
    else:
        target = args.output.expanduser()
        if target.is_symlink():
            parser.error('Output must not be a symbolic link.')
        if target.exists() and (not target.is_dir() or any(target.iterdir())):
            parser.error('Output must be absent or empty; existing output is never overwritten.')
        ROOT = target.resolve()
        if ROOT == SKILL or SKILL in ROOT.parents or ROOT in SKILL.parents:
            parser.error('Output must be outside the skill distribution.')
        ROOT.mkdir(parents=True, exist_ok=True)
    BOOT=SKILL/'scripts/bootstrap_project.py'
    VALID=SKILL/'scripts/validate_project.py'
    CASES=ROOT/'cases'
    CASES.mkdir(exist_ok=True)
    results=[]
    env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1')

    def js(path): return json.loads(path.read_text())
    def put(path,obj): path.write_text(json.dumps(obj,indent=2)+'\n')
    def write(path,text):
        path.parent.mkdir(parents=True,exist_ok=True); path.write_text(text)
    def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
    def artifact(p,rel): return {'path':rel,'sha256':sha(p/rel)}
    def records(p): return [json.loads(l) for l in (p/'audit/approvals.jsonl').read_text().splitlines() if l]
    def save_records(p,rs): (p/'audit/approvals.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in rs))
    def refresh(p,paths):
        rs=records(p)
        for r in rs:
            for a in r['artifacts']:
                if a['path'] in paths: a['sha256']=sha(p/a['path'])
        if 'evidence/extraction.csv' in paths:
            with (p/'evidence/extraction.csv').open() as handle:
                rows=list(csv.DictReader(handle))
            for r in rs:
                if r['kind'] in {'extraction','mapping'}:
                    keys=('item_id','field','value','unit','source_id','source_location','status')
                    r['verified_fields']=[{k:row.get(k,'') for k in keys} for row in rows if row.get('human_approval_id')==r['id']]
        save_records(p,rs)
        pr=js(p/'project.json')
        for state in ['data_freeze','release']:
            for a in (pr.get(state) or {}).get('artifacts',[]):
                if a['path'] in paths: a['sha256']=sha(p/a['path'])
        put(p/'project.json',pr)
    def rec(p,key,kind,paths,phase=None,scope='Synthetic fixture bounded batch; no real approval.'):
        r={'id':key,'kind':kind,'decision':'approved','actor_role':'human','actor_name':'SYNTHETIC TEST ACTOR — not a real person','decided_at':'2026-10-15T12:00:00Z','source_ref':'synthetic-test-fixture:no-real-decision','scope':scope,'protocol_version':'1.0','artifacts':[artifact(p,s) for s in paths]}
        if phase is not None:r['phase_id']=phase
        return r

    def run_validator(name,p,expected_reject,detail):
        r=subprocess.run([sys.executable,str(VALID),str(p),'--json'],capture_output=True,text=True,env=env)
        try: outcome=json.loads(r.stdout)
        except ValueError: outcome={'status':'CRASH','stdout':r.stdout,'stderr':r.stderr}
        if not isinstance(outcome, dict) or 'status' not in outcome:
            outcome={'status':'CRASH','stdout':r.stdout,'stderr':r.stderr}
        expected_status='FAIL' if expected_reject else 'STRUCTURAL_PASS'
        expected_exit=1 if expected_reject else 0
        matched=outcome['status']==expected_status and r.returncode==expected_exit
        result={'case':name,'path':str(p),'expected_reject':expected_reject,'status':outcome['status'],'exit_code':r.returncode,'meets_expectation':matched,'detail':detail,'result':outcome}
        results.append(result)
        (p/'test-result.json').write_text(json.dumps(result,indent=2)+'\n')
        return result

    def boot(name):
        p=CASES/name
        if p.exists() or p.is_symlink():
            raise FileExistsError(f'Refusing to replace an existing fixture: {p}')
        r=subprocess.run([sys.executable,str(BOOT),str(p),'--title','Synthetic integrity fixture','--language','en'],capture_output=True,text=True,env=env)
        if r.returncode:raise RuntimeError(r.stderr)
        return p

    def clone(name,base):
        p=CASES/name
        if p.exists() or p.is_symlink():
            raise FileExistsError(f'Refusing to replace an existing fixture: {p}')
        shutil.copytree(base,p)
        (p/'test-result.json').unlink(missing_ok=True)
        return p

    def mutate_project(p,func):
        pr=js(p/'project.json');func(pr);put(p/'project.json',pr)
    def mutate_records(p,func):
        rs=records(p);func(rs);save_records(p,rs)
    def make_completed(p):
        write(p/'protocol/PROTOCOL.md','# Synthetic protocol v1.0\nSoftware validation fixture; no scientific study or human approval.\n')
        write(p/'protocol/RULES.csv','rule_id,rule,rationale,source,test,approval_scope\nR1,Synthetic rule,Fixture construction,Test source,Fixture check,synthetic-only\n')
        write(p/'protocol/EXECUTION_PLAN.md','# Synthetic execution plan\nAll phases applicable for software testing only.\n')
        write(p/'evidence/extraction.csv','item_id,field,value,unit,source_id,source_location,status,human_approval_id,analysis_included\nitem-A,count,5,people,source-A,table 1,verified,extract-A,true\n')
        write(p/'evidence/source_registry.csv','source_id,stream,location,status\nsource-A,synthetic,Synthetic source location,retrieved\n')
        write(p/'analysis/inputs.csv','item_id,count\nitem-A,5\n')
        write(p/'publication/manuscript.txt','Synthetic manuscript version A — no scientific claims.\n')
        write(p/'publication/PUBLICATION_QA.md','# Synthetic QA\nFixture checks only; no actual publication QA or human review.\n')
        write(p/'CURRENT_STATE.md','# Synthetic fixture\nProtocol 1.0. Current phase 11. Release candidate for validator testing only.\n')
        write(p/'handoff/LATEST.md','Synthetic fixture. No real approval. Resume only software validation.\n')
        pr=js(p/'project.json');pr['protocol'].update(version='1.0',status='approved',approval_id='protocol-1');pr['current_phase']=11
        prot=['protocol/PROTOCOL.md','protocol/RULES.csv','protocol/EXECUTION_PLAN.md']
        rs=[rec(p,'protocol-1','protocol',prot,0)]
        for i in range(12):
            paths=prot if i==0 else (['publication/PUBLICATION_QA.md'] if i==11 else [f'qa/phase-{i}.md'])
            if i not in [0,11]:write(p/paths[0],f'Synthetic phase {i} gate evidence, software test only.\n')
            key='protocol-1' if i==0 else f'phase-{i}'
            if i:rs.append(rec(p,key,'phase_close',paths,i))
            pr['phases'][i].update(status='completed',applicability='applicable',gate_evidence=paths,closure_approval_id=key)
        extraction_approval=rec(p,'extract-A','extraction',['evidence/extraction.csv'],scope='item-A/count reviewed in synthetic fixture only')
        extraction_approval['verified_fields']=[{'item_id':'item-A','field':'count','value':'5','unit':'people','source_id':'source-A','source_location':'table 1','status':'verified'}]
        rs.append(extraction_approval)
        frozen=['evidence/extraction.csv','analysis/inputs.csv']
        rs.append(rec(p,'freeze-A','data_freeze',frozen))
        pr['data_freeze']={'protocol_version':'1.0','approval_id':'freeze-A','artifacts':[artifact(p,s) for s in frozen]}
        rel=['publication/manuscript.txt']
        rs.append(rec(p,'release-A','release',rel))
        pr['release']={'status':'release_candidate','approval_id':'release-A','artifacts':[artifact(p,s) for s in rel]}
        put(p/'project.json',pr);save_records(p,rs)

    baseline=boot('00-fresh-bootstrap')
    run_validator('fresh_bootstrap',baseline,False,'Unmodified scaffold must pass with draft warning; no scientific approval created.')
    full=clone('01-valid-synthetic-release',baseline);make_completed(full)
    run_validator('valid_synthetic_release',full,False,'All gate, protocol, extraction, freeze, and release hashes consistently represented; synthetic fixture only.')

    # Bootstrap behavior.
    for name,target in [('existing_nonempty',baseline),('symlink_destination',ROOT/'destination-link')]:
        if name=='symlink_destination':
            target.symlink_to(baseline,target_is_directory=True)
        r=subprocess.run([sys.executable,str(BOOT),str(target),'--title','Do not overwrite'],capture_output=True,text=True,env=env)
        results.append({'case':'bootstrap_'+name,'expected_reject':True,'status':'FAIL' if r.returncode else 'STRUCTURAL_PASS','exit_code':r.returncode,'meets_expectation':r.returncode!=0,'detail':r.stderr.strip()})

    # Negative cases caught by existing guards.
    def case(name,base,expected,detail,fn):
        p=clone(name,base);fn(p);run_validator(name,p,expected,detail);return p

    case('02-downstream-before-protocol',baseline,True,'Set current phase 1 and phase 1 in_progress with draft protocol.',lambda p: mutate_project(p,lambda x:(x.update(current_phase=1),x['phases'][1].update(status='in_progress'))))
    case('03-open-predecessor',full,True,'Reopen phase 7 while later phases remain completed.',lambda p:mutate_project(p,lambda x:x['phases'][7].update(status='in_progress')))
    case('04-wrong-phase-scope',full,True,'Phase 5 closure references approval with phase_id 4.',lambda p:mutate_records(p,lambda rs:next(r for r in rs if r['id']=='phase-5').update(phase_id=4)))
    case('05-ai-approval',full,True,'Change extraction actor role to ai.',lambda p:mutate_records(p,lambda rs:next(r for r in rs if r['id']=='extract-A').update(actor_role='ai')))
    case('06-rejected-approval',full,True,'Change protocol approval decision to rejected.',lambda p:mutate_records(p,lambda rs:rs[0].update(decision='rejected')))
    case('07-changed-protocol',full,True,'Modify protocol after its recorded hash.',lambda p:write(p/'protocol/PROTOCOL.md','Changed without reapproval\n'))
    case('08-changed-extraction',full,True,'Modify extraction after its recorded hashes.',lambda p:write(p/'evidence/extraction.csv',(p/'evidence/extraction.csv').read_text().replace(',5,',',50,')))
    case('09-changed-freeze-input',full,True,'Modify frozen analysis input after freeze hash.',lambda p:write(p/'analysis/inputs.csv','item_id,count\nitem-A,50\n'))
    case('10-changed-release',full,True,'Modify manuscript after release hash.',lambda p:write(p/'publication/manuscript.txt','Changed without approval\n'))
    case('11-missing-freeze-for-synthesis',full,True,'Remove data freeze with synthesis complete.',lambda p:mutate_project(p,lambda x:x.update(data_freeze=None)))
    case('12-critical-finding',full,True,'Add open critical QA finding after lock.',lambda p:put(p/'qa/findings.json',[{'id':'F1','severity':'critical','status':'open','detail':'synthetic defect'}]))
    case('13-unverified-included-extraction',full,True,'Included extraction row is ai_suggested, with current hashes.',lambda p:(write(p/'evidence/extraction.csv',(p/'evidence/extraction.csv').read_text().replace(',verified,',',ai_suggested,')),refresh(p,['evidence/extraction.csv'])))
    case('14-missing-source-location',full,True,'Included extraction row has no location, with current hashes.',lambda p:(write(p/'evidence/extraction.csv',(p/'evidence/extraction.csv').read_text().replace(',table 1,',',,')),refresh(p,['evidence/extraction.csv'])))
    case('15-snapshot-edit',baseline,True,'Edit pinned core.md without changing lock.',lambda p:write(p/'_pipeline/skill/references/core.md','Altered pinned rules\n'))
    case('16-snapshot-extra-file',baseline,True,'Add unexpected file in pinned snapshot.',lambda p:write(p/'_pipeline/skill/extra.txt','Unrecorded\n'))
    case('17-release-with-open-phase',full,True,'Leave phase 11 awaiting_human but release_candidate.',lambda p:mutate_project(p,lambda x:x['phases'][11].update(status='awaiting_human')))
    case('18-protocol-approval-incomplete-scope',full,True,'Remove RULES.csv from protocol approval artifacts.',lambda p:mutate_records(p,lambda rs:rs[0].update(artifacts=[a for a in rs[0]['artifacts'] if a['path']!='protocol/RULES.csv'])))
    case('19-phase-evidence-outside-scope',full,True,'Add unrelated gate file absent from phase closure artifacts.',lambda p:(write(p/'qa/extra.md','Unapproved evidence\n'),mutate_project(p,lambda x:x['phases'][3]['gate_evidence'].append('qa/extra.md'))))
    case('20-duplicate-approval-id',full,True,'Append duplicate approval ID.',lambda p:mutate_records(p,lambda rs:rs.append(rs[-1].copy())))
    case('21-invalid-approval-date',full,True,'Set a referenced approval date to garbage.',lambda p:mutate_records(p,lambda rs:rs[-1].update(decided_at='not-a-date')))
    case('22-artifact-path-traversal',full,True,'Release artifact points outside project.',lambda p:mutate_project(p,lambda x:x['release'].update(artifacts=[{'path':'../../outside.txt','sha256':'0'*64}])))

    # Approval scope and prior structural-bypass regression cases.
    def unrelated_approval(p,key):
        write(p/'qa/unrelated.txt','Reviewed unrelated item-B only.\n')
        mutate_records(p,lambda rs:next(r for r in rs if r['id']==key).update(artifacts=[artifact(p,'qa/unrelated.txt')],scope='Only item-B; explicitly excludes current item-A/data/manuscript',verified_fields=[]))
    case('23-extraction-approval-unrelated',full,True,'extract-A approves only unrelated file/item-B, yet row item-A/count references extract-A.',lambda p:unrelated_approval(p,'extract-A'))
    case('24-freeze-approval-unrelated',full,True,'freeze-A approves unrelated file while data_freeze.artifacts lists unapproved extraction/input files.',lambda p:unrelated_approval(p,'freeze-A'))
    case('25-release-approval-unrelated',full,True,'release-A approves unrelated file while release.artifacts lists unapproved manuscript.',lambda p:unrelated_approval(p,'release-A'))

    def snapshot_rehash(p):
        f=p/'_pipeline/skill/references/core.md';write(f,'Altered upstream rules without migration\n')
        lock=js(p/'PIPELINE_LOCK.json');lock['files']['references/core.md']=sha(f);put(p/'PIPELINE_LOCK.json',lock)
    case('26-snapshot-edit-lock-rehashed',baseline,True,'Edit pinned core.md and only lock hash; snapshot manifest still contains old digest and no migration recorded.',snapshot_rehash)

    def qa_without_freeze(p):
        def m(x):
            x['current_phase']=9;x['data_freeze']=None;x['release']={'status':'draft','approval_id':None,'artifacts':[]}
            for i in [10,11]:x['phases'][i].update(status='locked',closure_approval_id=None,gate_evidence=[])
        mutate_project(p,m)
    case('27-phase9-closed-no-lock',full,True,'Close phase 9 Scientific QA and data lock, keep phase 10 locked and data_freeze=None.',qa_without_freeze)

    def nonexistent_source(p):
        write(p/'evidence/extraction.csv',(p/'evidence/extraction.csv').read_text().replace(',source-A,',',source-NOT-IN-REGISTRY,'));refresh(p,['evidence/extraction.csv'])
    case('28-source-id-not-in-registry',full,True,'Included row source ID does not resolve in source_registry.csv.',nonexistent_source)
    case('29-missing-source-registry',full,True,'Delete source_registry.csv while included extracted data and release remain.',lambda p:(p/'evidence/source_registry.csv').unlink())

    def bad_csv(p):
        write(p/'evidence/extraction.csv','arbitrary,unrecognized,headers\nitem-A,ai_suggested,unverified\n');refresh(p,['evidence/extraction.csv'])
    case('30-malformed-extraction-schema',full,True,'Replace extraction schema with unrelated headers; require schema rejection.',bad_csv)

    def bad_bool(p):
        text=(p/'evidence/extraction.csv').read_text().replace(',verified,',',ai_suggested,').replace(',true\n',',true \n')
        write(p/'evidence/extraction.csv',text);refresh(p,['evidence/extraction.csv'])
    case('31-whitespace-included-bypass',full,True,'Included=true-space must still receive verification checks and reject ai_suggested status.',bad_bool)

    case('32-handoff-state-conflict',full,False,'MANUAL BOUNDARY: prose CURRENT_STATE contradicts project.json; structural pass is expected and requires human reconciliation.',lambda p:write(p/'CURRENT_STATE.md','# Current state\nProtocol: draft-0.1; NOT APPROVED. Phase: 0 in_progress. No data freeze. No release approval.\n'))
    case('33-current-phase-locked',baseline,True,'Set current phase 0 itself locked, leaving no active/available phase.',lambda p:mutate_project(p,lambda x:x['phases'][0].update(status='locked')))

    # Valid workflow branch and reopen path.
    def valid_phase1(p):
        def m(x):
            x['current_phase']=1;x['data_freeze']=None;x['release']={'status':'draft','approval_id':None,'artifacts':[]}
            for i in range(1,12):x['phases'][i].update(status='in_progress' if i==1 else 'locked',closure_approval_id=None,gate_evidence=[])
        mutate_project(p,m)
        write(p/'evidence/extraction.csv','item_id,field,value,unit,source_id,source_location,status,human_approval_id,analysis_included\n')
        save_records(p,[r for r in records(p) if r['id']=='protocol-1'])
    case('34-valid-phase1',full,False,'Protocol approved, phase 0 closed, current phase 1 in progress and later phases locked.',valid_phase1)

    def valid_not_applicable(p):
        def m(x):x['phases'][3].update(status='not_applicable',applicability='not_applicable',not_applicable_reason='Synthetic project design makes preliminary screening redundant')
        mutate_project(p,m)
        mutate_records(p,lambda rs:next(r for r in rs if r['id']=='phase-3').update(kind='not_applicable'))
    case('35-valid-not-applicable-phase',full,False,'Explicit non-applicability reason and matching scoped approval.',valid_not_applicable)

    case('36-extraction-with-draft-protocol',baseline,True,'Accepted analytic row is present while protocol remains draft and phase 0 current.',lambda p:(write(p/'evidence/extraction.csv',(full/'evidence/extraction.csv').read_text()),save_records(p,[dict(rec(p,'extract-A','extraction',['evidence/extraction.csv']),protocol_version='draft-0.1',verified_fields=[{'item_id':'item-A','field':'count','value':'5','unit':'people','source_id':'source-A','source_location':'table 1','status':'verified'}])])) )

    # Required paths must return structured failure when they escape the project.
    def escaped_required(p):
        f=p/'CURRENT_STATE.md';f.unlink();f.symlink_to(ROOT/'external-current-state.md');write(ROOT/'external-current-state.md','Outside project but inside allowed test-output directory\n')
    case('37-required-file-escape-crash',baseline,True,'Required CURRENT_STATE.md is a symlink outside the project: should cleanly return FAIL.',escaped_required)


    # Additional lock and schema boundaries.
    def frozen_open_critical(p):
        def m(x):
            x['current_phase']=9;x['release']={'status':'draft','approval_id':None,'artifacts':[]}
            x['phases'][9].update(status='in_progress',closure_approval_id=None,gate_evidence=[])
            for i in [10,11]:x['phases'][i].update(status='locked',closure_approval_id=None,gate_evidence=[])
        mutate_project(p,m)
        put(p/'qa/findings.json',[{'id':'critical-unverified-data','severity':'critical','status':'open','detail':'Synthetic unverified input defect remains unresolved.'}])
    case('38-freeze-with-open-critical',full,True,'Reject an approved freeze with open critical findings even while phase 9 is in progress and phase 10 locked.',frozen_open_critical)

    case('39-empty-extraction-file',full,True,'Truncate extraction.csv to zero bytes and renew synthetic artifact hashes.',lambda p:(write(p/'evidence/extraction.csv',''),refresh(p,['evidence/extraction.csv'])))
    case('40-unknown-findings-severity',full,True,'Reject unknown finding severity High rather than silently ignoring it.',lambda p:put(p/'qa/findings.json',[{'id':'F1','severity':'High','status':'open','detail':'Synthetic unresolved material conflict'}]))

    # Positive reopen and bounded row scope controls.
    def valid_reopen(p):
        def m(x):
            x['current_phase']=7;x['data_freeze']=None;x['release']={'status':'draft','approval_id':None,'artifacts':[]}
            for i in range(7,12):x['phases'][i].update(status='in_progress' if i==7 else 'locked',closure_approval_id=None,gate_evidence=[])
        mutate_project(p,m)
    case('41-valid-reopen-downstream-reset',full,False,'Reopen phase 7, lock all later phases, remove data freeze and release approval.',valid_reopen)
    case('42-wrong-verified-field',full,True,'Human extraction approval lists item-B/count but included row is item-A/count.',lambda p:mutate_records(p,lambda rs:next(r for r in rs if r['id']=='extract-A')['verified_fields'][0].update(item_id='item-B')))
    case('43-protocol-version-mismatch',full,True,'Change project protocol version without renewing dependent approval scopes.',lambda p:mutate_project(p,lambda x:x['protocol'].update(version='2.0')))

    put(ROOT/'results.json',results)
    summary={'output':str(ROOT),'skill':str(SKILL),'total':len(results),'met_expectation':sum(r['meets_expectation'] for r in results),'unexpected_passes':[r['case'] for r in results if r['expected_reject'] and r['status']=='STRUCTURAL_PASS'],'crashes':[r['case'] for r in results if r['status']=='CRASH'],'unexpected_results':[r['case'] for r in results if not r['meets_expectation']],'manual_boundaries':['32-handoff-state-conflict']}
    put(ROOT/'summary.json',summary)
    print(json.dumps(summary,indent=2))
    return 0 if all(result['meets_expectation'] for result in results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
