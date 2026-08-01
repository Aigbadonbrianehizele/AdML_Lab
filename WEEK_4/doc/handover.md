# Week 4 Handover — M1 Math/Tensors

## Environment state
## Environment state
- OS: Windows 11
- Python: 3.13
- venv: C:\Users\DELL\Documents\AdML_Lab\venv
- Installed numpy into the venv this week — required to run week4_check.ps1 and all four Week 4 modules

## Commits this week
git log --oneline shows duplicate commits from a git recovery event (diverged branches — parallel local + GitHub-web edits merged via 2bb0e3d). History is NOT clean; several commits (e.g. linalg_foundations.py, tensor_ops.py, log.md broadcasting entries) appear 2-6 times under near-identical messages.

Verified: current working tree content is correct — diffed duplicate pairs against HEAD and confirmed the intended final version won the merge (e.g. linalg_foundations.py's break-fix demo block is correctly commented out, matching Wednesday's intent). tensor_ops.py confirmed clean via week4_check.ps1 passing.

Not done: full history cleanup (interactive rebase/squash) — deferred, not required for Week 5 to start, but flagged as technical debt below.

Full log:
2bb0e3d (HEAD -> main, origin/main, origin/HEAD) Merge branch 'main' of https://github.com/
Aigbadonbrianehizele/AdML_Lab
f0d883d week-4-wed: comment out live break-fix demos, log.md audit progress — M1
7139d6a week-4-mon: tensor_ops.py — broadcasting/einsum/shape algebra — M1
255dbf0 week-4-mon: log.md — broadcasting failure cases 1-3, Tusday test injections — M1   
3332c01 week-4-wed: comment out live break-fix demos, log.md audit progress — M1
78160b5 week-4-wed: week4_check.ps1 side quest — M1
2597efe week-4-tue: loss_landscape.py — gradient descent + failure modes — M1
5b25413 week-4-mon: tensor_ops.py — broadcasting/einsum/shape algebra — M1
8b525a5 week-4-sun: gradients.py — numerical gradient/Jacobian/chain rule — M1
1e07581 week-4-sat: linalg_foundations.py — vectors/matrices/norms/SVD — M1
d77a3df week-4-sat: linalg_foundations.py — vectors/matrices/norms/SVD — M1
532a4d7 week-4-mon: log.md — broadcasting failure cases 1-3, Tusday test injections — M1   
54cfdf9 week-4-mon: tensor_ops.py — broadcasting/einsum/shape algebra — M1
073584c week-4-mon: tensor_ops.py — broadcasting/einsum/shape algebra — M1
c63c879 "week-4-mon: tensor_ops.py — broadcasting/einsum/shape algebra — M1"
351f35a week-4-mon: log.md — broadcasting failure cases 1-3 — M1
96b8a69 week-4-mon: tensor_ops.py — broadcasting/einsum/shape algebra — M1
72948a6 week-4-sun: gradients.py — numerical gradient/Jacobian/chain rule — M1
9232429 week-4-sun: gradients.py — numerical gradient/Jacobian/chain rule — M1
828a708 week-4-sat: linalg_foundations.py — vectors/matrices/norms/SVD — M1

## Deliverables: completed vs open
**Completed:**
- linalg_foundations.py — vector ops, norms, matrix_multiply, add_bounded_perturbation, top_singular_direction (4/5, verified against hand-solutions with np.allclose)
- gradients.py — mse_loss, mse_loss_gradient, numerical_gradient, jacobian (4/5, gradient-check confirmed True, jacobian-vs-W confirmed True)
- tensor_ops.py — flatten_batch, channel_mean, normalize, einsum patterns (5/5, week4_check.ps1 passes clean, three broadcasting failures documented with verbatim tracebacks)
- loss_landscape.py — gradient_descent, sgd_with_momentum, all 4 injections run with verbatim output and causal analysis (4/5)
- week4_check.ps1 — side quest, runs all four modules, reports pass/fail
- log.md — audited for verbatim output, causal WHY, exact fix, transferable principle (4/5)
- P1.1–P7.2 problem set — solved on paper before code, per gate rule

**Open / not done:**
- P8.1 (FGSM first-principles derivation) — not yet attempted; needs its own fresh, undistracted session, not squeezed into an already-long Thursday
- Wednesday Hour 3 — 5-question log.md audit — consciously skipped this week due to time constraints
- M2 connection field — left blank on every loss_landscape.py injection and log.md entry; deliberately not backfilled with a connection not yet genuinely understood
- PGD connection (Thursday self-assessment prompt) — left open for the same reason

## Open technical debt (be honest)
- Duplicate commit history on main from git recovery (parallel local/GitHub-web edits, merged via 2bb0e3d) — content verified correct, history itself not cleaned up
- SVD derivation gap: cannot yet derive from first principles why U[:,0]/S[0] pair as the max-amplification direction (same category as the Tuesday matrix-inverse gap) — currently reasoning via pattern/metaphor, not proof
- top_singular_direction never verified against np.linalg.svd output directly (only the six hand-rolled functions were cross-checked)
- Wednesday Hour 3 (5-question log.md audit) skipped due to time constraints
- M2 connection field blank across loss_landscape.py and log.md — not filled because the actual connections aren't understood well enough yet to state honestly

Note: gradient-check verification (gradients.py) and some loss_landscape.py injection write-ups were completed retroactively during Thursday's self-assessment rather than at time of writing — the underlying work and results are sound, this is a documentation-timing gap, not unresolved debt.

## Starting command for Week 5 Saturday
1. Verify environment: activate venv, confirm `python -m week_04.linalg_foundations` (and the other three modules) still run clean via week4_check.ps1 before starting new work
2. Pull latest from origin/main, confirm working tree clean (`git status`) before making any new edits — do not repeat the parallel local/web-edit pattern that caused this week's git recovery
3. [Week 5 module name/file — TBD, insert once Week 5's plan is generated/received]
4. Close open technical debt items where relevant before building on top of them — specifically the SVD derivation and top_singular_direction verification, since Week 5+ (M1 continues through W8) will likely build on this week's linear algebra work

## Math foundations covered — one sentence on each:

### Linear algebra: vectors/matrices/norms/SVD
Implemented and cross-checked vector ops, L1/L2/L-infinity norms, and matrix multiplication against hand-solved math; can reconstruct SVD's W=UΣVt shape algebra and correctly identify U[:,0]/S[0] as the max-amplification direction, but still can't derive from first principles why that pairing holds — open gap carried into Week 5.

### Calculus: partial derivatives/chain rule/Jacobians
Verified mse_loss_gradient against a finite-difference numerical_gradient (matched to tolerance) and jacobian() against a known W; worked the full two-layer backprop derivation (P4.2) correctly piece-by-piece but never assembled dL/dx into one final closed-form line.

### NumPy: broadcasting/einsum/shape algebra
Strongest section this week — triggered and documented three real broadcasting failures with verbatim tracebacks, correctly diagnosed the mismatched axis in each using right-aligned shape comparison, and confirmed all modules run clean via week4_check.ps1.

### Optimisation: gradient descent/momentum/failure modes
Ran and causally explained all four break-fix injections with verbatim output: lr=10.0 divergence traced to eigenvalue-scaled error blowup, non-positive-definite A traced to mixed-sign eigenvalues causing net divergence despite a decreasing loss curve, gradient-check confirmed the analytical gradient correct, and momentum=0.99 traced to overshoot-driven decaying oscillation rather than a bug.