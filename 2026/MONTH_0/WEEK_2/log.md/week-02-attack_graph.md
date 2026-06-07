## WEEK 2 — INJECTION 1

**Exact error:**
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\CLONE\attack_graph.py", line 105, in <module>
    g2.topological_sort()
    ~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\Documents\CLONE\attack_graph.py", line 61, in topological_sort
    raise ValueError("cycle detected")
ValueError: cycle detected

**Exact fix:**
There is no fix here we are testing to see code is functioning properply, meaning that our code is following protocol.

**Causal WHY:**
There is a cycle cause C(the last node) traverses back to A the source node. Normally when we hit C we are supposed to HIT BLACK based off the fact that we have exausted every node but since C traverse A meaning continuous path means we have a repeating loop around of node so while we have exhausted the nodes the loop will forever run meaning GRAY

**Transferable principle:**
In the real world attackers must validate their script to see if runs before applying it to our victim model, because when using methods like FGSM and GCG silent breaks can cause the payload or script to be ineffective when tested against the victim model, because cycles cause the process to stall and breaks the order of you attack surface e.g FGSM and GCG thus causing errors.

**ATLAS justification:**
AML.T0002: The attacker must ensure that payload has internal checks to detect cycles that disrupt the reading when using attack surfaces like FGSM and GCG 

# WEEK 2 - INJECTION 2
**Exact error:**
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\CLONE\attack_graph.py", line 103, in <module>
    g3.cheapest_path('X','Y')  # ValueError — not crash
    ~~~~~~~~~~~~~~~~^^^^^^^^^
  File "C:\Users\DELL\Documents\CLONE\attack_graph.py", line 85, in cheapest_path
    raise ValueError
ValueError

**Exact fix:**
There is no fix here we are testing to see code is functioning properply, meaning that our code is following protocol.

**Causal WHY:**
There is no edge between node X and node Y cause they don't exist as neighbors in the self.graph container, as dist is assumed to be infinity at for all nodes except from the source node but since there is no edge the distance will remain infinity that will trigger the value error

**Transferable principle:**
Whenever you traverse a graph to prepare an attack, always make sure the nodes are connected via edges.

**ATLAS justification:**
AML.T0002 — As an attacker you must ensure when relating datasets, make sure the datasets are contextualized thus we can take steps to ensure thing by triggering errors where set conditions are not met


# WEEK 2 - INJECTION 3

**Exact error:**
No error instead 
Injection 3 Result: (0.1, ['A', 'B'])

**Exact fix:**
There is no fix here we are testing to see code is functioning properply, meaning that our code is following protocol.

**Causal WHY:**
When you look at the payload add_edge only checks if src exists and does not check for destination thus we will have multiple same destinations in an src if possible.

**Transferable principle:**
When a data structure silently accepts duplicates the correctness depends on the implementation in the code that check for  little errors, not the data structure it self

**ATLAS justification:**
AML.T0002 - Alex Birisian used an attack surface like this, he published an his own package with the same name as a popular package, so when pip picks up it checks public PyPI before it looks at internal libraries.
 

# WEEK 2 - INJECTION 4
**Exact error:**
True

**Exact fix:**
There is no fix here we are testing to see code is functioning properply, meaning that our code is following protocol.

**Causal WHY:**
This is because the node has an edge that s directed towards itself so when we have a continuous chain or in progress and GRAY would have it we have a cycle.Node traverses itself it still counts as a cycle.

**Transferable principle:**
Whenever you traverse a graph to prepare an attack, always make sure the nodes are not containing self loops, cause it causes and infinite path that basically stalls the process

**ATLAS justification:**
AML.T0002 - The attacker can use the payload(containing a self node traversal) to cause an infinite loop on the command slowing down the process thereby creating a smokescreen to buy time for the real attack. - Birsan class
