## INJECTION 1 — CYCLE DETECTION — UBER DATA BREACH
**OUTPUT:**< IT CRASHED BECAUSE OF VALUEERROR >
**EXPECTED:**< I expected it to return IT CRASHED BECAUSE OF VALUEERROR >
**WHY THIS BEHAVIOUR:**< It behaves like this because a cycle has been detected so there is no independet loop causing topological_sort(Kahn's algorithm) to crash>
**EXACT FIX**< There is no need for a fix>
**TRANSFERABLE PRINCIPLE:**< Think of a payload as a signal and the ML pipeline the system that loop dues to cyclic behaviour, they will function as a closed loop system where the Adversary feeds a signal(payload) into the system and the system returns a feedback(more info on the system) this helps the adversary to optimize the payload as he get better information on the system after each feedback loop>
**ATLAS AML T.0002:**< After the attacker takes advantage of the closed loop system he can gather data such as model parameter, weights or training datasets, which the attacker can use to strip away the models invisibilty(Safety guardrails)>

## INJECTION 2 - SILENT OMISSION OF A NODE - UBER DATA BREACH
**OUTPUT:**<
[('recon', 1)] 1.8571 True
[('env_audit', 1), ('recon', 1)] 1.5228 False
[('env_audit', 1), ('model_probe', 1), ('recon', 1)] 1.63805 False
[('env_audit', 1), ('fgsm_attack', 1), ('model_probe', 1)] 2.01215 True
[('env_audit', 1), ('fgsm_attack', 1), ('model_probe', 1)] 2.3596500000000002 False
[('data_collect', 1), ('env_audit', 1), ('fgsm_attack', 1)] 2.74295 True
[('data_collect', 1), ('env_audit', 1), ('fgsm_attack', 1)] 1.78715 False>

**EXPECTED:**< I expected this to return in this format>
**EXACT FIX**< There is no need for a fix>
**WHY THIS BEHAVIOUR:**< Normally we are supposed to see exfil represented in the the output but it was omitted using attack_vector.remove('exfil') since freq_map never saw it top_n never saw it eitjer so therefore no print>
**TRANSFERABLE PRINCIPLE:**< Silent failures are more dangerous tahn crashes, because crashes actually notify and can tell you the type of error, silent one other hand you might not know until you manually check yourself.>
**ATLAS AML T.0002:**< For an Adversary when trying to parse the artifacts(acquired dataset similar to model data ) if you leave out one of the artifacts it will cause the generate output(payload) to be ineffective depending on the importance>


## INJECTION 3 - UNDERSIZED CIRCULAR BUFFER - UBER DATA BREACH
**OUTPUT:**<{
  "execution_order": [
    "recon",
    "env_audit",
    "data_collect",
    "model_probe",
    "fgsm_attack",
    "pgd_attack",
    "transfer",
    "exfil"
  ],
  "attack_frequencies": {
    "recon": 1,
    "env_audit": 1,
    "model_probe": 1,
    "fgsm_attack": 1,
    "pgd_attack": 1,
    "transfer": 1,
    "data_collect": 1,
    "exfil": 1
  },
  "final_loss_window": [
    0.8749,
    0.6656
  ],
  "converged": true,
  "timestamp": "2026-05-20T11:59:10.082500"
}>
**EXPECTED:**< I expected this to return in this format>
**WHY THIS BEHAVIOUR:**< The final_Loss_window only returns two losses the last two infact because the buffer has a length of two>
**EXACT FIX**< There is no need for a fix>
**TRANSFERABLE PRINCIPLE:**< Always check the buffer size before trusting the convergence metrics cause the few(2) statitcal data point is never useful>
**ATLAS AML T.0002:**< When Adversaries are using methods such as FGSM to find vunerabilities in a victim model, you need to make sure that the convergence metrics are statistcally correct meaning the dataset must must have a large enough surface are to produce a meaningul metric thus creating a specialized payload>


## INJECTION 4 - DELETED DIRECTORY - UBER DATA BREACH
**OUTPUT:**<
PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\SUNDAY_PART_1> python pipeline.py
[('recon', 1)] 2.6786 True
[('env_audit', 1), ('recon', 1)] 2.20045 False
[('env_audit', 1), ('model_probe', 1), ('recon', 1)] 2.4053666666666667 False
[('env_audit', 1), ('fgsm_attack', 1), ('model_probe', 1)] 2.066075 False
[('env_audit', 1), ('fgsm_attack', 1), ('model_probe', 1)] 1.8199999999999998 False
[('env_audit', 1), ('fgsm_attack', 1), ('model_probe', 1)] 1.51948 False
[('data_collect', 1), ('env_audit', 1), ('fgsm_attack', 1)] 1.34954 False
[('data_collect', 1), ('env_audit', 1), ('exfil', 1)] 1.04956 True
PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\SUNDAY_PART_1> >
**EXPECTED:**< I expected this to return in this format>
**EXACT FIX**< There is no need for a fix>
**WHY THIS BEHAVIOUR:**< Even after the directory is deleted using os library we are able to create a new directory and there was no crash>
**TRANSFERABLE PRINCIPLE:**< When an Adversary is operating in an environment it is best to assume it is unstable as your filesystems can be be changed, damaged, or moved hence your your pipeline can crash mid-execution because of these what-ifs so for protection it is best that you makes use of exist_ok=True to make sure the pipeline keep running even after a break>
**ATLAS AML T.0002:**< An Adversary can turn a victim model attack into a feedback loop session so he can optimize his payload, while his payload runs and returns data that will be used to optimize the payload continuously we must make sure to employ exist_ok=True so that the pipeline runs properly so that we don't encounter breaks mid session because there can be path change, file damage or even deletion >
