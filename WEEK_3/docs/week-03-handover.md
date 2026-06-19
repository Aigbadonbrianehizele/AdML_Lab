## Week 3 Handover — June 17, 2026

### Environment state
- OS: WINDOWS 11
- Python: 3.13.14
- venv: C:\Users\DELL\Documents\AdML_Lab\venv (active)
- Repo: Aigbadonbrianehizele/AdML_Lab
- Working Directory: C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src
- Run command: python -m <module>

### Commits this week (paste git log --oneline)
PS C:\Users\DELL\Documents\AdML_Lab> git log --oneline
9ba33cc (HEAD -> main, origin/main, origin/HEAD) docs: add week-03 log to WEEK_3/docs
7270c55 docs: add week-03 incident card to WEEK_3/docs
4c2d1f4 chore: remove week-03 incident card from wrong directory
430764a docs: add Week 3 incident card skeleton AML.T0010.001+AML.T0010.003
98784fb Update env_auditor.py
ec21cef week-3-wed: supply_chain_checkerv2.py — AML.T0010.001 + AML.T0010.003
188fddf week-3-tue: safe_runner.py — Log4Shell class process injection — AML.T0010
1eebc27 Update supply_chain_checker.py
3aff5b7 week-3: consolidate all files into WEEK_3/src/week_03 — AML.T0010
510731a week-3: restore deleted files — AML.T0010
ce7d315 week-3: remove duplicate 2026 folder — AML.T0010
f3a05d5 Rename model_loader.py to model_loaderv1.py
2a11efe week-3-mon: dep_resolver.py - Birsan class resolver attack - AML.T0010
af47d8d week-3-sun: model_loader.py scanner fixed + supply_chain_checker.py — pickletools opcode scan — AML.T0010
38483c2 week-3-sat: model_loader.py + env_auditor.py hardened - AML.T0010
18b4fc7 week-3-sat: env_auditor.py hardened - module level calls removed - AML.T0010
643e1e4 week-3-sat: model_loader.py + env_auditor.py - Hugging Face+SolarWinds class - AML.T0010
3871768 fix: remove MONTH_0 from tracking
89bd24a fix: remove submodule, track MONTH_0 as regular directory
8bed4b0 week-3-sat: model_loader.py + env_auditor.py - Hugging Face+SolarWinds class - AML.T0010
59ed819 Update week-02-self-assessment.md

### Deliverables: completed vs open
Completed:
- model_loader.py — pickletools opcode scanner
- env_auditor.py — environment fingerprinting
- supply_chain_checker.py — integration gate
- dep_resolver.py — dependency graph attack vector
- safe_runner.py — subprocess security
- incident-card.md — Weekend recap
Open:


### Open technical debt
- model_loader.py: no context-aware opcode pairing — APPENDS+GLOBAL/REDUCE combination not detected
- Flask/Django deployment flagged by SAMTL BACKEND ENGINEER — not in scope for Week 3, revisit when pipeline needs a web interface


### Starting command for Week 4 Saturday
python -m week_04.<module>

### MITRE ATLAS covered
AML.T0010.001 + AML.T0010.003 — Poisoned Dependency & Software Compromise: Built a tool that detects malicious payloads, audit environment integrity, validates dependency graphs,- Same attack surface as Hugging Face, SolarWinds, Birsan Dependency Attack, CodeCov Bash Uploader, Log4Shell.