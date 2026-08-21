# CAN-CCHD Phase 5 — Schema Clarification 01: `transitional_nonactionable_n`

Date: 2026-08-21  
Branch: `phase5-extraction`  
Status: **BINDING CLARIFICATION; NO CHANGE TO LOCKED OUTCOME DEFINITIONS**

## Why this clarification is needed

The Phase 5 v0.1 extraction matrix contains the field `transitional_nonactionable_n`. Its label is narrower than the locked Protocol Core category `NON_CAN`, which includes not only transitional physiology but also other explicitly non-actionable/incidental findings.

Some primary reports also provide an aggregate negative clinical-outcome class such as “no significant non-CCHD disease” without distinguishing healthy infants from minor/transitional findings.

## Binding interpretation for v0.1

For the v0.1 matrix and all Phase 5 extraction blocks using its column set:

> `transitional_nonactionable_n` is the **aggregate participant-level `NON_CAN` count**.

It may include:
- transitional/physiologic findings;
- incidental non-actionable diagnoses;
- minor findings without qualifying management consequence;
- a primary-source aggregate explicitly establishing absence of the review's clinically relevant/actionable outcome, when healthy status cannot be claimed.

The raw diagnosis fields and extraction notes must state which of these situations applies.

A value in `transitional_nonactionable_n` must **not** be interpreted as proof that every included infant had transitional circulation.

`explicitly_healthy_no_diagnosis_n` remains separate and may be used only when the primary source affirmatively supports healthy/no-diagnosis status.

`unknown_unascertained_n` remains separate and is used when outcome/diagnosis is not ascertained or is insufficiently reported to determine participant-level CAN-CCHD status.

## Future presentation

A later consolidated matrix version may rename this field to `non_can_n` and optionally add diagnostic subtypes. Until then, this clarification preserves compatibility with the frozen 76-row v0.1 matrix without changing any scientific classification rule.
