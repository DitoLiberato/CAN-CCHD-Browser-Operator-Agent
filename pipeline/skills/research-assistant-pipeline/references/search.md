# Search design and source collection

## Build queries for this question

Derive concepts from the approved question and appropriate framework (PICO, PECO,
PCC or another justified structure). Do not force every concept into the query if
that loses relevant evidence. Consider controlled vocabulary, free text, historical
names, spelling, abbreviations and relevant languages. Translate syntax for each
platform; do not assume one query works everywhere.

Choose sources based on the topic/design and access. Distinguish bibliographic
databases, full-text repositories, registries, regional sources, citation indexes
and metadata enrichment. Overlapping sources are not independent coverage claims.
Record restrictions and rationale, not convenient defaults.

Present candidate searches and tradeoffs to the researcher. Pilot exact syntax,
inspect noise and known eligible sentinel retrieval, and refine with logged reasons.
Sentinels are checks, not proof of exhaustive recall. Failure can expose search or
sentinel problems; investigate. Do not overfit queries to support a favored conclusion.

## Execution and provenance

Log each run in `evidence/search_log.csv`: ID, stream, protocol version, source,
platform, query verbatim, filters, execution date, URL/API, access mode, native count
if observed, exported/imported counts, raw artifact path/hash, status and limitations.
Leave unknown counts blank with an explanation. Preserve the original export.

Record platform-native searches separately from general-web discovery. Never claim
Embase/Scopus/etc. were searched because a web engine found indexed snippets. A search
result snippet is not verified full text. Source access denied is not zero results.
Log failed/partial queries and pagination or export caps. Document manual imports.

Perform only legal/authorized retrieval. Let the user handle login and access barriers;
never store credentials in project files or bypass access restrictions. Offer manual
exports when automation is unavailable. Do not email authors without explicit permission.

Keep planned and actual source status distinct. A source can be completed, partial,
unavailable, awaiting export or closed with an approved limitation. Systematic review
claims require the agreed coverage and transparent deviations; do not silently
downgrade a review because the current AI lacks a tool.

## Expansion and closure

Use backward/forward citation chasing and targeted expansion if justified. Record
wave/source/seed and new candidates. Set stopping criteria in the protocol; saturation
in supplementary discovery is not proof of database completeness. Reopen only for a
new signal, update plan or documented reason, not to endlessly accumulate hits.

Record the last actual search date and generate exact supplementary strategies from
the run log. Reconcile PRISMA counts from preserved events; do not reverse-engineer
unknown initial counts from a final corpus. Distinguish exploratory probes, formal
searches, updates and post-hoc targeted searches throughout.
