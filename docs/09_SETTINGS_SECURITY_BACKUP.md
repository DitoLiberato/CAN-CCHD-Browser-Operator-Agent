# Settings, Credentials, Security, and Backups

## .env
Create `.env.example`. Never commit `.env`.

Required settings:
```text
NCBI_EMAIL=
NCBI_TOOL=can_cchd_browser_operator_agent
NCBI_API_KEY=
CROSSREF_MAILTO=
SEMANTIC_SCHOLAR_API_KEY=
LLM_PROVIDER=gemini
GEMINI_API_KEY=
GEMINI_MODEL=gemini-2.5-flash
OPENAI_API_KEY=
OPENAI_MODEL=
BROWSER_MODE=headless
DOWNLOAD_DIR=data/downloads
SNAPSHOT_DIR=data/evidence_snapshots
DB_PATH=data/processed/can_cchd_agent.db
BACKUP_DIR=data/backups
```

## .gitignore
Include:
```text
.env
.env.*
!.env.example
data/processed/
data/backups/
data/downloads/
data/evidence_snapshots/
*.sqlite
*.db
__pycache__/
```

## Credentials Rules
Do not log API keys, passwords, session cookies, or authentication tokens.

Supervised login:
```text
user logs in manually
agent never asks for password
agent resumes after user clicks Continue
```

## Backups
The app must offer:
```text
Create database backup
Download latest backup
List backups
Restore from backup, optional later
```
Create backup before bulk duplicate merge, large import, analysis dataset rebuild, or schema migration.

Backup filename:
```text
can_cchd_agent_YYYYMMDD_HHMMSS.db
```

## Codespaces Warning
Show in UI:
```text
Closing the forwarded port does not delete the database.
Stopping/restarting the same codespace should preserve files.
Deleting the codespace deletes local files unless backed up/exported.
Create database backups regularly.
```

## Safety Boundaries
The app must not bypass paywalls, bypass CAPTCHA, automatically submit credentials, download illegal copies, use shadow libraries, hide failed searches, or hide unresolved QA warnings.

## Acceptance Criteria
Settings are complete when `.env.example` exists, `.env` is ignored, credentials are masked in UI, connection tests exist, backup/download exists, supervised login never stores passwords, and audit logs never include secrets.
