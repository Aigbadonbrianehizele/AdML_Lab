## FINDING 001 - ROCK YOU CLASS 
**REAL WORLD CLASS:**< RockYou 2012 credential stuffing breach>
**SEVERITY:**< MEDIUM>
**DESCRIPTION:**< ROCKYOU2012 is breach were over 32 million pairs of passwords and usernames were stolen from ROCKYOU's database, in the real world ROCKYOU is a dummy runner or thirdparty attack, I'll get to that later. It was propagated using simple sql queries, I said dummy runner before, it means it was never the main goal, the detour had to be taken cause that was the easiet route rather than facing a fortress like a Bank. So after getting these 32 million pairs the attackers where able to compare the passowrds and cluster them to makes frequencies so the highest frequency value where launched first to the real victim(main goal) using a sort of brute force technique called credential stuffing, blue teamers know its worse when you have multiple databases meaning even more passwords. >
**PROOF OF CONCEPT:**< 
build_frequency_map([])
{}>
**ROOT CAUSE:**< Because there is no condition set for when the input is empty >
**FIX APPLIED:**< No fix needed as the code is correct by design>
**Residual Risk:**< Silent failures if there is an incomplete dataset or an empty dataset >
**ATLAS AML T.0002:** < The attacker acquires datasets similar to the attack surface and merges it then ranks them by frequency of occurence creating the payload and then uses creditential stuffing technique to throw the payload at the victim model(ROCKYOU) >


## FINDING 002 - BIRSAN CLASS
**REAL WORLD CLASS:**< PyPI Dependency Confusion attack — 2021 — Alex Birsan.>
**SEVERITY:**< CRITICAL>
**DESCRIPTION:**< Alex Birsan the GOAT himself. He found out that you could manipulate the install packages for npm and pip, And because of that he was able to access the systems of multiple enterprise and he did by taking advantage of PyPI vunerabilities he was able to add his malicious packages into python packages gaining him access.>
**PROOF OF CONCEPT:**<python
g2 = AttackGraph()
    for n in ['A', 'B', 'C']:
        g2.add_node(n)
    g2.add_edge('A', 'B', 1.0)
    g2.add_edge('B', 'C', 1.0)
    g2.add_edge('C', 'A', 1.0)
    print("Injection 1 has_cycle:", g2.has_cycle())  # Expected: True
    try:
        g2.topological_sort()
    except ValueError as e:
        print(f"Injection 1 topological_sort raised ValueError: {e}")
> 
**ROOT CAUSE:**< A cycle is accepted, as add_edge has no trigger for cycle detection, then topological_sort() method has spotted that there is no independent node hence it triggers a cycle detected response>
**FIX APPLIED:**< No fix needs to be applied, because the behaviour is by design> 
**Residual Risk:**< Provided an attacker id trying to running pipeline.py and it skips topological_sort and goes straight to scheduling if add_edge contains a cycle it will be fed fed into the scheduler silently  > 
**ATLAS AML T.0002:** < When an adversary is trying to execute pipeline and he then forgets to add topological_sort() method it can use a silent failure in scheduler provided add_edge() method contains a cycle this will cause the payload to ineffective >


## FINDING 003 - UBER DATA BREACH
**REAL WORLD CLASS:**< Uber 2016 data breach — GitHub S3 credential leak + unvalidated integration.>
**SEVERITY:**< CRITICAL>
**DESCRIPTION:**< Three components work together in isolation credential,S3 bucket and git repo. Integrating them creates the breach. So no integration tested what the bucket contained or who could acess it>
**PROOF OF CONCEPT:**< BASH: Remove-Item -Recurse -Force output
test_injection.py: os.makedirs("output" , exist_ok = True)> 
**ROOT CAUSE:**< The /output directory never actually existed. without exist_ok=True os.makedirs  it would throw FileExistsError or FileNotFoundError and crash the pipeline mid executtion. The real problem is that in reality /output never existed and pipeline assumed it existed.>
**FIX APPLIED:**< No fix needs to be applied, because the behaviour is by design> 
**Residual Risk:**< Provided the fix (os.makedirs("output" , exist_ok = True)) is applied you could still run into problem with missing parent directory disk space and write permissions> 
**ATLAS AML T.0002:** < When an adversary is trying to execute pipeline.py and he forgets to include (os.makedirs("output" , exist_ok = True)) the pipeline will crash mid execution>