## April 12, 2026 · WEEK 2 · SAT · frequency_oracle.py

### Baseline 1

**What I ran:**
words = ['FGSM','PGD','FGSM','GCG','PGD','FGSM','CW','GCG','FGSM']
top_n(build_frequency_map(words), 3)

**Exact output:**
[('FGSM', 4), ('GCG', 2), ('PGD', 2)]

**Why it looks like this:**
So what build_frequency_map() function
does is that it tasks a list uses items and frequency of each item to create a dict and then the top_n() function then rearranges them in descending order using key if key is equal use item name so have to classify them as strings and you can the odd ('GCG', 2), ('PGD', 2) it is like because even though the values are the same we can use str(item) to sort them in ascending order that is you see GCG come before PGD even though values are identical so G come first
**Transferable principle:**
frequency maps reveal which targets to prioritze, whether the target is a password or a vector

**ATLAS: AML.T0002** — 
Adversarial explots become easier when the attacker can access dataset that resemble the victim thus making use of frequency maps give the attacker a more exploitable path in victim's model


### Baseline 2
**What I ran:**
words = ['FGSM','PGD','FGSM','GCG','PGD','FGSM','CW','GCG','FGSM']
merge_maps({'a':3, 'b': 1}, {'b': 2, 'c': 5})

**Exact output:**
{'a': 3, 'b': 3, 'c': 5}

**Why it looks like this:**
It looks like this because we are map merging, so in this case if look at the code the statement tell us if key is te same in both maps you should merge, a and b appeared 3 times, c appeared 5. Merging give you true total 


**Transferable principle:**
Merging maps tells the attacker which patterns(passwords or vectors depending on the model) is most exploitable


**ATLAS: AML.T0002**
Adversarial exploits become easier for attackers when they have mutiple datasets they utilize to atake advantage of a victim model, by using merge maps they are able to utilize frequency and using the frequency to find more exploitable patterns in the victim model


### BASELINE 3

**What I ran:**
invert_map({'FGSM':4, 'PGD':2, 'GCG': 2,'CW':1})

**Exact output:**
{4: ['FGSM'], 2: ['PGD', 'GCG'], 1: ['CW']}

**Why it looks like this:**
Remember we use invert_map function is for switching position of dict elements I mean key and value. This is done by intializing a new dict and changing the normal position by manipulating keys and value and then items will be saved as lists and when ever two items have the same count they will appended.'


**Transferable principle:**
invert_map is a function that lets you groups different exploits by their frequency, thus grouping vectors with same frequency. For a dict the usual format is {item: count} and since we invert and define iteam in an [] it turns to a list {counts: [item]}

**ATLAS: AML.T0002**
For an attacker an inverted map were the different exploits are grouped by frequency data. invert_map is grouping effective exploits in terms of frequency. This is effectively ranking dangerous vector and attacker can use to comprise the victim model.


### --- BREAK-FIX INJECTIONS ---###
 
### INJECTION 1A
**What I ran:**
build_frequency_map([])

**Exact output:**
 {}

**Why it looks like this:**
When you look at the structure of our code it convert a list to a dict by turning each element in the list to a key and assigning a value by frequency. So since there is an empty list your will also get an empty dict 

**Transferable principle:**
an attack payload that fails on null input failes silently mid opertaion  corrupting the data(frequency map,passwords) before they get to the model. Attack payload must be rendered sufficient enough before it can go live(the victim model)
**ATLAS: AML.T0002**
Automated attack scripts must be able to return empty containers, rather than return errors so as to verify the scripts work offline before they are tested on the actual model.

### INJECTION 1B
**What I ran:**
top_n({}, 3)

**Exact output:**
[]

**Why it looks like this:**
The code is built to convert a dict into a list but as the dict is an empty container the list will also be an empty container. We use for loops to call the .items() and place them in the new list and then start appending keys and values and preferably in order


**Transferable principle:**
Due to the fact that our script returns an empty container we can conclude that we have no payload to use the victim model. Therefore we must ensure that we have enough datasets(Frequency maps) to constitute a payload

**ATLAS: AML.T0002**
Automated attack scripts must be able return a payload rather an empty container, thus we can conclude there is no dataset(frequency maps) that we use to manufacture the payload. So you must make sure you have an actual payload that works offline before one go live.

### INJECTION 2
**What I ran:**
top_n({'FGSM':4, 'PGD':2}, 10)

**Exact output:**
[('FGSM', 4), ('PGD', 2)]

**Why it looks like this:**
When we call the top_n function it slices the dataset(a dict that is convert to a list using for loops) and brings out the first set of dataset depending the instrucion of the slice which in this case is [:10] but since the is list is not up to [:10] we slice through as many as possible. So basically slicing is just calling the items in the list using indexes.

**Transferable principle:**
Due to the fact that our script fires a rather incomplete dataset, we can conclude that have an incomplete payload and we need the complete dataset(i.e more than 10 indexes), so we need a system that validates the payload before firing, because when the attacker ventures into the model which likely will have a lockout threshold, the stronger sets that are capable of breaking the model might never be used.

**ATLAS: AML.T0002**
An automated attack script that fires an incomplete payload fires no payload why the actual dataset might not be part of the incomplete payload. So we must make sure that our code works offline before we go into a live test

### INJECTION 3
**What I ran:**
build_frequency_map([0.1+0.2, 0.3, 0.30000000000000004])

**Exact output:**
{0.30000000000000004: 2, 0.3: 1}

**Why it looks like this:**
When you look at the code it doesn't really hit you in the face, cause there is only one value that is (0.30000000000000004) and yet we have 2 as the frequency so what is happening here? IEEE 754, see systems read the numbers as binary and this 0.1 and 0.2 in IEEE 754 have several decimal places when you see 0.1 and 0.2 the backend sees several numbers after the decimal point so the frequency 2 comes from (0.30000000000000004) and (0.1 + 0.2) because approximately (0.1 + 0.2) is equal to (0.30000000000000004) than (o.3), cause in IEEE 754 (0.3) is reading like (0.29999999999999999999). 

**Transferable principle:**
This is a case of suboptimal perturbation, where input(dataset) cause a performance degradation. Here we have a dataset that has an error(floating corruption) causing the final payload to degraded. The floating arithmeticproduces wrong frequencies for the dataset hence this leads to performance degradation. Eventually when the frequencies of the dataset is ranked and feed into the script it will produce s suboptimal payload that will likely have an adverse effect on the attack

**ATLAS: AML.T0002**
Here we have ingested a dataset that mirrors the attack surface(the victim model) and we have parsed the dataset incorrectly due to floating arithmetic so eventually we will have sub optimal payload so we fail to adversarial attempt at the attack surface

### INJECTION 4 PART 1
**What I ran:**
merge_maps(a, b)

**Exact output:**
{'x': 3}

**Why it looks like this:**
Look at the code we are combining the different datasets using and empty dict and for loops so combine them by adding the key and value pairs to the empty and if a pairs have the same key just add the values 

**Transferable principle:**
It is imprtant to gather as much datasets as possible that mirror the attack surface so to properly utilize them merging the datasets will improve the performance of the dataset that constitutes the payload. So basically for an attack like Rockyou having 

**ATLAS: AML.T0002**
For an attacker is it best when you have access to mutiple datasets that mirror the attack surface so as to produce a variations of payloads or the attacker can merge the datasets and create a more complex payload rather than having mutiple payloads that can work.

### INJECTION 4 PART 2
**What I ran:**
((Mutation check, should be {'x': 1}):", a)

**Exact output:**
(Mutation check, should be {'x': 1}): {'x': 1}

**Why it looks like this:**
By looking at the code you can tell that when a(variable) is called that holds a dict so when a is called you can expect get the {'x': 1}. An if you look at our even after merging a wasn't mutated because in the code a new empty  dict is created at the beginning so that a and b do not overwrite each other

**Transferable principle:**
This is allows the attacker maintain the original datasets so as to allow him to recall them later to be use a payload for a possible new model or new attack variant

**ATLAS: AML.T0002**
Using the empty dict method to create a an space for merging datasets so that the attacker can avoid overwriting dataset so he can make use of said datasets new attacks.
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
## Injection 1 — Pop Empty Heap — Mirai Class

**Error:** **File "C:\Users\DELL\Documents\CLONE\Minheap_AttackScheduler.py", line 62, in <module>
    empty.pop()
    ~~~~~~~~~^^
  File "C:\Users\DELL\Documents\CLONE\Minheap_AttackScheduler.py", line 16, in pop
    root = self.tree[0]
           ~~~~~~~~~^^^
IndexError: list index out of range**
**Fix:** < We wrap the code within the pop function with a trigger, in this case we use raise to trigger an exception when the array has a length of zero 
        if len(self.tree) == 0:
            raise IndexError
        else:
            i = len(self.tree) - 1    
            root = self.tree[0]
            self.tree[0] = self.tree[i]
            self.tree.pop(i)
            self._sift_down()
            return root>
**Why it crashed:** < It crashed because pop function is used to remove elements from indexes, in an array so since the array we using pop on is an empty container we will trigger an IndexError >
**Transferable principle:** < Bounds checking failure: This occurs when a the script tries to access an index that is outside the valid range>
**ATLAS AML T.0002:** < Adversaries usually make use of chain of payloads(scripts) similar to agentic workflows, if a prior payload returns an empty dataset the current payload will try to sort an empty container so we need to employ triggers in place to ease the process>

## Injection 2 — Priority Queue  — Mirai Class
**Output:**<
(0.1, 'A')
(0.1, 'B')
(0.1, 'C')>

**Expected:**< I expected it to turn out like that as that is format> 
**Why this behaviour:**< This happened because the indexes cannot fufill the condition self.tree[i] < self.tree[j] hence there is no swap>
**Transferable principle:**< Provided we have a situation where the heap only sorts based on priorities, we need to add a second filter layer if the priorities are the same. This second would best work as a counter that increments for elements inserted into the array>
**ATLAS AML T.0002:** < The Adversaries, when they want run a chain of payloads that fetch datasets, They might get datasets that have the same priorities, so we need to add a second layer that seperates the datasets based of the insertion, so what we are doing is trying to sort our dataset cause we taking data from public sources and unsecure buckets>



## Injection 3 — Negative - Priority Queue  — Mirai Class
**Output:**<
(-1.0, 'exploit')
(0.5, 'probe')>

**Expected:**< I expected it to turn out like that as that is format>
**Why this behaviour:**<-1.0 is a float thus the comparison self.tree[i] < self.tree[j] works whether positive or negative>

**Transferable principle:** < The script is built to handle negative float parameters as it follows self.tree[i] < self.tree[j], so incase the script doesn't make provisions for negative float changes should be made. If negative floats are invalid add a guard, else the script should document them explicitly >
**ATLAS AML T.0002:**< For an Adversarial Engineer creating a script that compares negatives priorities is required as the most effective of payloads usually are negative float numbers.>


## INJECTION 4 - POP INSUFFICIENT HEAP - Mirai Class
**Error:**<Traceback (most recent call last):
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\MONDAY\MinHeap_AttackSchedulerFIX.py", line 86, in <module>
    sched4.next_attack()
    ~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\MONDAY\MinHeap_AttackSchedulerFIX.py", line 52, in next_attack
    return self.heap.pop()
           ~~~~~~~~~~~~~^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\MONDAY\MinHeap_AttackSchedulerFIX.py", line 16, in pop       
    raise IndexError
IndexError>

**Fix:**< if self.heap.is_empty():
            raise IndexError
        else:
            return self.heap.pop()>
**Why it crashed:**< It crashed because we tried to pop an empty container on the second turn, because we called sched4.next_attack twice the system and there was only one item in the container so on the second turn it wil break.>

**Transferable principle:** < Bound Checking Failure: This occurs when a script tries to access an index that is none existent, in this case this occurs during the second next.attack as there is only one item in the container>
**ATLAS AML T.0002:** < When employing a chain of attack vectors, if a prior vector returns an insufficient dataset, the current vector will try to sort on the dataset so because of this we need to employ triggers for possible outcomes in the vector. >



## Injection 1 — Zero Capacity Buffer — Google Brain Incident
**Error:**<
PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\TUESDAY> python loss_buffer.py
[2.1] mean: 2.1
[2.1, 1.9] mean: 2.0
[2.1, 1.9, 1.7] mean: 1.9000000000000001
[2.1, 1.9, 1.7, 1.5] mean: 1.8
[2.1, 1.9, 1.7, 1.5, 1.3] mean: 1.7
[1.9, 1.7, 1.5, 1.3, 1.1] mean: 1.5
[1.7, 1.5, 1.3, 1.1, 0.9] mean: 1.3
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\TUESDAY\loss_buffer.py", line 47, in <module>
    CircularLossBuffer(0).push(1.0)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\TUESDAY\loss_buffer.py", line 10, in push
    self.buffer[self.write_index] = loss
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
    IndexError: list assignment index out of range>

**Fix:**< Wrap the push method in a conditional statement using if, hence we add a condition to make the method run if the capacity is not equal to zero
    def push(self, loss: float):
        if self.capacity != 0:
            if self.current_size == self.capacity:
                self.buffer[self.write_index] = loss 
                self.write_index = (self.write_index + 1) % self.capacity
            else:
                self.buffer[self.write_index] = loss
                self.write_index = (self.write_index + 1) % self.capacity 
                self.current_size = self.current_size + 1 >    
**Why it crashed:**< capacity = 0, [None]* 0 is 0 thus self.buffer = [], thus causing causing and Indexerror when trying to call push method >
**Transferable principle:**< Bound Checking Failure: This occurs when the script is trying to access an index that is out of range or in this case has no range as the buffer is a zero capacity buffer >
**ATLAS AML T.0002:**< Adversaries usually use chains of scripts to sort out datasets or data structures and if one the prior scripts in the chain produces an incomplete or more precisely an empty dataset, when te next script tries to process the empty it will run into an IndexError >

## INJECTION 2 - Overwrite Validity - Google Brain Incident
**Output:**< [3.0] >
**Expected:**< I expected the result to be three as the the script was programmed to return 3.0 >
**Why this behaviour:**< This happens because the current_size is equal to capacity and a new element is about to enter buffer thus the oldest element must make way the newest one. >
**Transferable principle:**< In an fixed entry stucture such as a buffer, when full, the oldest entries is always removed to make way for the newest one, when dealing with methods like FGSM looping if the early loss rate(which reveeals the convergence) is greater than the buffer capacity it cause convergence failure silently>
**ATLAS AML T.0002:**< When Adversaries collect data from sources be it public(public spaces on the internet) or private(vunerable buckets) the goals is to have a large attack surface that can use to optimize the payload, hence if you use fixed entry strcture like a buffer provided the capacity of the buffer is less than the acquired data this will lead to loss of important data that should be use to train and optimize the payload>

## INJECTION 3 - Mean on Empty Buffer - Google Brain Incident
**Output:**<0.0>
**Expected:**< I expected it to break lowkey cause cause every value starts at None and since no values are defined but it produce 0.0 as the result>
**Why this behaviour:**< Because the value of current_size(filled spaces in the buffer) is zero the mean method returns 0.0>
**Transferable principle:**< When dealing with datasets understand that you need to add guards to ensure that the script doesn't try to read empty dataset as it can cause silent failure leading to erroneous payload(output)>
**ATLAS AML T.0002:**<  Adversaries need to ensure that datasets(relative to victim model) that will be used to optimize a payload are not empty becasue when the script reads data the empty dataset it can cause erroneous payloads>

## INJECTION 4 -    Threshold vs (Maximum - Minimum) -  Google Brain Incident
**Output:**<True>
**Expected:**< I expected True as the answer cause min and max take initial values of i when i = 0 >
**Why this behaviour:**< Because the maximum and minimum values are initially self.buffer[0], 1.0 - 1.0 is zero and then since threshold is greater than zero we return True>
**Transferable principle:**< Always check current_size before trusting converging metrics because a single data point is never statistically meaningful>
**ATLAS AML T.0002:**< When Adversaries are using methods such as FGSM to find vunerabilities in a victim model, you need to make sure that the convergence metrics are statistcally correct meaning the dataset must must have a large enough surface are to produce a meaningul metric thus creating a specialized payload >
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
## Week 2 Self-Assessment

frequency_oracle.py quality (1-5 + justification):I had to rate it 1 because manual implementation with no optimization, makes it run slowly, but this is expected with starte code.
attack_scheduler.py quality (1-5 + justification):I had to rate it 1 because _sift_down() method was causing an infinite loop when I first ran pipeline.py because j = (2*i) + 1 was mssing for the two swaps
attack_graph.py quality (1-5 + justification):I rate 1 because the truth while the code shows promise it would be slow compared to industry standarc which probably has dedicated libraries
loss_buffer.py quality (1-5 + justification):Honestly I liked this one this it was short direct but the thing is it not industry standard
pipeline.py quality (1-5 + justification):The most fun I have ever had I got to do samething twice and it was good but the main drawback is that we have to import methods for scripts that are not industry standard
log.md quality (1-5 + justification):I rated it 2 because we are still beginning we are really well versed with this but with time we get sharper vocabularies and better descriptions with time and more confidence in our skill
What I would do differently if Week 2 started again: Be more serious, but even laziness is part of the process
What the circular buffer taught me about Month 2 FGSM: Convergence metrics and how we need to scale it to the size of the buffer for better accuracy
What the graph traversal taught me about Month 2 autograd: Using traversal Autograd explains to use how data commuincates with machines that process them for data to come out as output. AI is used to make a mental map of machines that touched the data, provided there is any noise in the input the AI goes backward to the every first machine to check were the problems are. 


Note: Remember not being industry quality is part of the process we are learning to understand how to represent our understanding using syntax using libraries would make it to damn easy.
