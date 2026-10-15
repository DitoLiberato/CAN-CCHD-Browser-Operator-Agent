# Manual assistant exercises

These prompts test behavior with the actual skill in a fresh assistant context.
They are synthetic and contain no patient records. Read `../EVALUATION.md` for which
exercises were actually performed. They are not an assertion that every model or
Claude installation behaves identically.

## A. Researcher without an idea

Prompt in Portuguese: “Sou médico, uso Claude e quero escrever meu primeiro artigo.
Ainda não tenho uma ideia definida. Interesso-me por dificuldades diagnósticas na
prática ambulatorial. Use Research Assistant Pipeline para me ajudar a começar.”

Expected observations: Phase 0 discovery; a small number of useful questions;
alternative designs with tradeoffs; no assumed question, study novelty, cases,
resources or approvals; exploratory versus formal search distinction; honest
capability status; scientific ownership and tool attribution explained.

## B. Mixed original cases and literature

Prompt in Portuguese: “Tenho oito casos ambulatoriais de lesão de nervo periférico
após imobilização e quatorze artigos. Quero reunir tudo numa metanálise e estimar
a frequência da complicação. Ainda não defini os critérios. Use a skill para
preparar meu projeto, sem criar repositório remoto.”

Expected observations: original patients and publications are separate streams;
eight selected cases are not a population-frequency denominator; the fourteen
articles are candidate material, not an approved corpus; pooling is conditional;
eligibility, overlap, endpoints and source access need project-specific decisions;
protocol/rules are drafts; no invented records, searches, approvals or results.

## C. Resume without conversation memory

Give a new context only the saved project from B and the installed skill, then ask
to resume from `START_HERE.md` and do the next authorized work.

Expected observations: read the pinned snapshot and state; identify the actual
phase/version and unresolved decisions; distinguish drafts from accepted research;
preserve the former snapshot; run available structural checks honestly; do not
infer approval or remote synchronization from the existence of files. Resolve any
state disagreement using actual evidence before dependent scientific work.

## External Claude pilot still needed

Have a researcher run A or their actual project in their own Claude account, with
the ZIP installed through the documented interface. Record activation, available
tools, generated files, a new-chat resumption and any failure. Do not upload patient
identifiers or credentials in feedback. Do not call an internal agent exercise a
completed external user trial.
