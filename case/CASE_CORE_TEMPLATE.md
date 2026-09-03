# CASE CORE TEMPLATE — KEEP PATIENT-SPECIFIC VERSION PRIVATE UNTIL PRIVACY CLEARANCE

**Status:** template only  
**Purpose:** reconstruct the index case from primary clinical sources before literature interpretation.

> Do not commit a filled patient-specific copy to this public repository until privacy/consent review explicitly permits it.

## A. Source registry

For each source:

- source_id;
- source_type;
- relative date/time;
- author/service if scientifically needed;
- whether original source is available;
- privacy status;
- notes.

## B. Baseline

- age/age band;
- sex;
- gestational context if relevant;
- weight/growth if relevant;
- syndromic/genetic diagnoses;
- known congenital anomalies;
- baseline anatomy/physiology;
- prior procedures/medications.

## C. Timeline

For each event:

- relative timepoint;
- observed event;
- objective data;
- diagnosis/differential at that time;
- intervention;
- response;
- source_id;
- verification status.

## D. Key investigations

### Imaging

For each study:

- modality;
- relative time;
- indication;
- raw report findings;
- author-adjudicated normalized findings;
- images available yes/no;
- source_id.

### Laboratory/microbiology

- test;
- relative time;
- result;
- clinical context;
- source_id.

### Physiology

- oxygenation;
- ventilation/blood gas;
- hemodynamics;
- respiratory support;
- other relevant objective measurements.

## E. Intervention ledger

For every proposed/performed intervention:

- intervention;
- status: `considered | planned | attempted | performed | aborted`;
- relative time;
- rationale documented contemporaneously;
- technical result;
- immediate clinical response;
- delayed response;
- complication;
- source_id.

**Rule:** planned is never converted to performed without primary-source verification.

## F. Diagnostic attribution ledger

For each important symptom/event, keep separate:

- observed fact;
- contemporaneous clinician attribution;
- competing explanations;
- later author interpretation;
- certainty level.

## G. Outcome/follow-up

- discharge status;
- oxygen/respiratory status;
- cardiac status;
- feeding/growth;
- later procedures;
- rehospitalization;
- follow-up duration;
- unresolved issues.

## H. CARE completeness check

Track:

- patient information (de-identified);
- clinical findings;
- timeline;
- diagnostic assessment;
- therapeutic intervention;
- follow-up/outcomes;
- discussion-ready strengths/limitations;
- patient/guardian perspective if feasible;
- informed consent status.

## I. Freeze checklist

`CASE_CORE_v1.0` may be frozen only when:

- major timeline conflicts are resolved or explicitly marked;
- all central facts have source provenance;
- planned vs completed procedures are unambiguous;
- final manuscript endpoint has adequate follow-up or a documented decision to use an earlier endpoint;
- missing information remains explicitly missing;
- human physician verification is complete.
