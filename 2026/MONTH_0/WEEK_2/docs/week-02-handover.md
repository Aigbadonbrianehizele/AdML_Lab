## Week 2 Handover — April 12–18, 2026

## Environment state
Windows 11, Python 3.13, repo at C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0

## Commits this week
[paste git log --oneline after commits are made]

## Deliverables: completed vs open
✅ frequency_oracle.py
✅ attack_graph.py
✅ attack_scheduler.py
✅ loss_buffer.py
✅ pipeline.py
✅ week-02-incident-card.md
✅ log.md entries (4+ injections per session)
✅ week-02-self-assessment.md not consolidated — scattered across session folders

## Open technical debt
- Filenames: MinHeap_AttackSchedulerFIX.py renamed to attack_scheduler.py but OG file still present
- sys.path.insert hacks in pipeline.py instead of proper package imports
- log.md scattered across MONDAY/TUESDAY/SUNDAY_PART_2/THURSDAY folders

## Starting command for Week 3 Saturday
python WEEK_2/src/week_02/pipeline.py

## MITRE ATLAS covered
AML.T0002 — built frequency maps, graphs, heaps, and circular buffers as ML attack primitives matching adversarial artifact acquisition and pipeline construction techniques.