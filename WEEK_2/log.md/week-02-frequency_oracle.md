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