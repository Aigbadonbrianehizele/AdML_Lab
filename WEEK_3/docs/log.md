## May 31st, 2026 - WEEK 3 - SAT PART 1 - model_loader.py


### Injection 1

**Exact error:**
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\model_loader.py", line 43, in <module>
    print(scan_pickle('C:/Users/DELL/tmp/does_not_exist.pkl'))
          ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\model_loader.py", line 15, in scan_pickle
FileNotFoundError

**Exact Fix:**
if not os.path.exists(filepath):
  raise FileNotFoundError

So the file line of the fix os.path.exists() is a special method that checks for existence so paired with if not, it means if file path doesn't exist, from line 2 raise a FileNotFoundError

**Causal WHY:**
When os make makes the syscall to the physical memory if the filepath doesn't exist, python will raise a FileNotFoundError

**Transferable principle:**
Before a script can be executed, the file path must exist(full file validattion). 

**ATLAS: AML.T0010.003**
A pre-flight scanner that crashes on invalid input doesn't justify the file as malicious content.


### Injection 2
**Exact error:**
(venv) PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03> python model_loader.py
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\model_loader.py", line 48, in <module>
    print(audit_report('/tmp/empty.pkl'))
          ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\model_loader.py", line 35, in audit_report
    audit = scan_pickle(filepath)
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\model_loader.py", line 18, in scan_pickle
ValueError

**Exact fix:**
if os.path.getsize(filepath) == 0:
    raise ValueError


**Causal WHY:**
An empty file contains no opcodes hence dangerous_count returns 0, since dangerous count is 0 risk_level returns CLEAN, and then the safe_to_load returns True because risk_level returns CLEAN.

**Transferable principle:**
Our pre flight scanner should be able to discern between and empty file and a file with size that's like loading empty bottle for shipment when it has no content it's just waste.

**ATLAS: AML.T0010.003**
A pre filght scanner that accepts an empty file(pytorch model) it risks reducing the accuracy of the ML supply chain or environment

 

### Injection 3
**Exact error:**
PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03> python model_loader.py
[{'opcode': 'INST', 'offset': 2}, {'opcode': 'INST', 'offset': 5}, {'opcode': 'APPENDS', 'offset': 14}]

**Exact fix:**
No fix needed here.

**Causal WHY:**
Because some of the letters trigger the scan_pickle() method which filters out dangerous opcodes , so its aggressive because it searches byte by byte


**Transferable principle:**
The pre flight scanner works a bit too well cause if looks at meaningful sentences like the example we wrote into the file and it calls some bytes out as dangerous

**ATLAS: AML.T0010.003**
Because of pre flight scanner to aggressive("works to well") it will often lead to many false positives and these reduces the accuracy of the ML supply chain or environment



### Injection 4
**Exact error:**
Output: 5518 dangerous opcodes found, risk_level: MALICIOUS, safe_to_load: False
Scanner did not crash. Full output truncated — 5518 entries.
**Exact fix:**
No fix needed
**Causal WHY:**
The function audit_report() method is used to police through the entire file byte by byte for the joined values like 9934 it will shred it to single byte and police through it and because the sample space is 100k intergers we get a dangerous_count is 5518
**Transferable principle:**
This large result shows us that our scanner is trustworthy enough to check through large model
**ATLAS: AML.T0010.003**
The pre flight scanner is rigorous enough to handle large files meaning that it would aid the accuracy and security of the ML supply chain.


## May 31st, 2026 - WEEK 3 - SAT PART 2 - env_auditor.py
### Injection 1
**Exact error:**
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\env_auditor.py", line 52, in
 <module>
    print(flag_unpinned('C:/Users/DELL/tmp/nonexistent_req.txt'))
          ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\env_auditor.py", line 34, in
 flag_unpinned
    with open(requirements_path) as f:
         ~~~~^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/DELL/tmp/nonexistent_req.txt'



**Exact fix:**
if not os.path.exists(requirements_path):
  raise FileNotFoundError(f"Requirements file path not found {requirements_path}")


**Causal WHY:**
The fucntion flag_unpinned made no check for existence before calling open() so when the OS file returned not-found, python raised FileNotFoundError and the terminal called a Traceback on FileNotFoundError


**Transferable principle:**
An unhandled crash during a pre flight security check means the pipeline either stalls or proceeds without completing. Either way the gate failed. So it because of that any threat on the system will be missed

**ATLAS: AML.T0010**
Provided a threat is missed courtesy of an unhandled crash it causes the entire pipeline to be infected my malicious actors mkaing the  product dangerous for example Solarwind Sunburst 2020


### Injection 2
**Exact error:**
[]

**Exact fix:**
No fix needed

**Causal WHY:**
The flag_unpinned to returns an empty container [] solely because the file in the path is empty

**Transferable principle:** A pre flight scanner should be able to return an empty container if the file being read is empty, rather than silently crash as this affect our ML supply chain

**ATLAS: AML.T0010**
When flag_unpinned returns an empty container [] because in the case the file was empty because of that we can't have pinned or unpinned files so our scanner needs to be able to check the size of the file before even scanning.

### Injection 3
**Exact error:**
['pytest']

**Exact fix:**
no fix needed
**Causal WHY:**
Because flag_unpinned weeds out dependencies that have no version number the version number is acompanied by either '=='or '>=' or '~=' by reading line by line checking for certain conditional triggers if '==' not in line and '>=' not in line and '~=' not in line: it reads True so the line is appended to list 



**Transferable principle:**
A pre flight scanner should be able should to be read through a dependency list and different packages by their version as undeclared version can proved to malicious code just waiting


**ATLAS: AML.T0010**
The pre flight scanner must be capable of thorough checking for unpinned dependencies in a requirement path, else an attacker will be capable of intercepting the specific packages that have no version and install malicious payload in those version. So these check must be made regularly even adding importlib.metadata.distribution to two step with the requirement text constantly else our ML supply chain can be corrupted


### Injection 4
**Exact error:**
No error


**Exact fix:**
No fix needed


**Causal WHY:**
The reason why we have no error is because "exist_ok = True" stops the FileExistsError when you are trying to create a directory that already exists and it help to create a directory that doesn't exist so it also stops FileNotFoundError 

**Transferable principle:**
A pre filight scanner must be able to store all the contents of its last check in a particular path and if that path doesn't exist employ "os.makedirs" and 'exist_ok = True" to create a path to store the final information on the check


**ATLAS: AML.T0010**
A pre flight scanner must be capable of storing data taken during check in a file so that the data can be cross refernced with the next check, overwriting of previous data or deletion of content will make it harder to track safety of the virtual environment puttinhg the ML supply chain at risk of silent corruption by threat actors


## June 1st, 2026 - WEEK 3 - SUN PART 1 - supply_chain_checker.py
### REVIEW oOF CODE
Our script cannot be too aggressive because we need to also send code into the CI pipeline and they might not get in so instead of a BLOCK and locking them out we put a WARNING and then we scan the code properly before we let it into the pipeline, if the code isn't clean then BLOCK but the system would have been better with more security checks like network or system checks maybe using AD can get us by that but having many safety guards ain't bad.


Our code still runs even when there is no file path or there is an empty file because the code says risk_level must be MALICIOUS first so that the safe_to_proceed is False.
 
Our model_loader.py file takes byte reading to far it reads every single byte not opcode positions. This can be corrected by making use of pickle and pickletools library but this exercise forbids pickle.load() so we employ pickletools.dis()

APPENDS is a false positiive because it normal intially malicious but could be if paired with GLOBAL or REDUCE

I also learnt that can't call a condition twice for elif even if you are and-ing in the next block  

So we need to add a boolean to our code to identify if file exists or not, so we introduce file_found to toggle as True or False depending on where the file exists

We also changed the procedures, before "SUSPICIOUS" meant you could still pass with a warning attached to it, but here is thee problem all the attacker needs is one dangerous opcode either "REDUCE" or "GLOBAL" to gain control so we blocked it, although it would have been far better to say if SUSPICIOUS and the opcode is GLOBAL or REDUCE, or without the if SUSPICIOUS, just GLOBAL or REDUCE, would be enough to call safe_to_proceed as False.

If you notice we permit code run when we have unpinned dependencies but allow code to crash when the file is empty, this is dangerous especially because of Alex Birsan Fortune 500 Goldrush so we need to add triggers for when there are unpinned dependencies to block

shutil is a library that is used for file manipulation, rmtree means remove tree or directory and then ignore_error = True makes sure the terminal throws no error in case there is an issue we deletion

The file env_auditor's get_python_info(), specifically the in_venv within it doesn't propery check if you are in a virtual environment furthermore it assume that you must create a virtual environment within the global environment, so if the virtual environment is the global environment(basically a global-virtual environment) it reads not a virtual environment, funny enough according to the logic there is no difference between a global-virtula environment and even a normal global environment they are all the same.


### CLAUDE'S REVIEW
OPEN DESIGN ITEM — pre_flight_check safe_to_proceed logic
Current: SUSPICIOUS blocks (count-based, 1-2 dangerous opcodes).
Proposed: block on GLOBAL/REDUCE presence regardless of count, since either
alone is sufficient for RCE via __reduce__. Count-based threshold is weaker
than opcode-type-based threshold.
Status: NOT IMPLEMENTED. Deferred — out of time this session.
Next step: check found opcodes against {REDUCE, GLOBAL}, set safe_to_proceed
False if present, regardless of risk_level. Decide whether risk_level itself
(in model_loader.py) should also reflect this, or whether pre_flight_check
adds a separate block_reason field.

### INJECTION 1
**Exact error:**
C:/Users/DELL/tmp/ghost.pkl doesn't exist
{'env_snapshot': {'python_info': {'version': '3.13.13', 'executable': 'C:\\Users\\DELL\\Documents\\AdML_Lab\\venv\\Scripts\\python.exe', 'platform': 'win32', 'in_venv': True, 'venv_path': 'C:\\Users\\DELL\\Documents\\AdML_Lab\\venv'}, 'installed_packages_count': 1}, 'unpinned_deps': None, 'pickle_scan': {'risk_level': 'MALICIOUS', 'dangerous_count': 0, 'opcodes_found': [], 'file_found': False}, 'safe_to_proceed': False, 'warnings': [], 'timestamp': '2026-06-11T10:34:19.001831'}

**Exact fix:**
No fix needed


**Causal WHY:**
From the output you can see that the file doesn't exist, and even at that the script doesn't crash because we use "try" and "except" to catch the error FileNotFoundError and prints "C:/Users/DELL/tmp/ghost.pkl doesn't exist" and thus the pre_flight_check is able to run. Then you can find the information "'file_found': False" within pickle_scan, the purpose of it is to trigger as True or False depending on the existence of the file in this case non existent means False is the read. Before the old code would print MALICIOUS based on the risk_level to block it making sure it wouldn't mislead the user because we never ran the file but we called it malicious, so adding file_found and changing triggers on the elif block would make sure we have no dead code. 



**Transferable principle:**
The problem of a non existent file triggering a MALICIOUS statement can often be misleading and these type of inconsistency can cause unwarranted alarms, this reduces integrity of the scanner.



**ATLAS: AML.T0010.001 + AML.T0010.003**
Under AML.T0010.001 + AML.T0010.003 a scanner that labels both "non existent file" and a "malicious file" detection the same way trains operators to ignore or distrust MALICIOUS alerts, so when a real compromised file reaches the checkpoint it might get dismissed as a false positive




### INJECTION 2
**Exact error:**
Traceback (most recent call last):
  File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\supply_chain_checker.py", line 53, in <module>
    print(pre_flight_check('/tmp/benign.pkl', '/tmp/no_such_req.txt'))
          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\supply_chain_checker.py", line 11, in pre_flight_check
    unpinned = flag_unpinned(requirements_path)
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\env_auditor.py", line 33, in
 flag_unpinned
    raise FileNotFoundError(f"Requiremnts file path not found {requirements_path}")
FileNotFoundError: Requiremnts file path not found /tmp/no_such_req.txt


**Exact fix:**
try:
   unpinned = flag_unpinned(requirements_path)
except FileNotFoundError as e:
  unpinned =  None
  warnings.append("The requirement path can't be found") 


**Causal WHY:**
The pre_flight_check tries to access a path using the flag_unpinned function and since the function pre_flight_check never actually validates the external pipeline dependency that script consumes it propagates an unhandled exception.



**Transferable principle:**
A proper scanner should be able to block an operation where the any external dependency that the pipeline component consumes must be validated at the module boudndary before execution proceeds, else an unhandled exception can crash the script, producing no log and leaving the environment unverified. 



**ATLAS: AML.T0010.001 + AML.T0010.003**
Under AML.T0010.001(Dependency Injection) + AML.T0010.003(Malicious model upload) the scanner should be able to validate pickle model(AML.T0010.003) and software dependencies (AML.T0010.001) existence at the modular boundaries before execution else it can cause and unhandled exception where the operation is killed leaving no forensic data(logs) to be analyzed by operators, this leaves a special exception where the attacker can upload malicious content(pickle model) before directing the script to a non existent dependency path ,this is a full-file validation bypass that was used to by HuggingFace detectors


### INJECTION 3
**Exact error:**
SAFE TO PROCEED
{'env_snapshot': {'python_info': {'version': '3.13.14', 'executable': 'C:\\Users\\DELL\\Documents\\AdML_Lab\\venv\\Scripts\\python.exe', 'platform': 'win32', 'in_venv': True, 'venv_path': 'C:\\Users\\DELL\\Documents\\AdML_Lab\\venv'}, 'installed_packages_count': 1}, 'unpinned_deps': None, 'pickle_scan': {'risk_level': 'CLEAN', 'dangerous_count': 0, 'opcodes_found': [], 'file_found': True}, 'safe_to_proceed': True, 'warnings': [], 'timestamp': '2026-06-12T15:31:07.735049'}

**Exact fix:**
No fix is needed



**Causal WHY:**
The scanner is tested against "shutil.rmtree('output', ignore_errors = True)" and the directory file still gets created because we added a safeguard "os.makedirs(os.path.dirname(output_path), exist_ok = True)" that ensures that even if directory doesn't exist it will be created hence the function pre_check still produces the .json log file.


**Transferable principle:**
A script that writes output files should never assume that it's target directory exists, it should always check for the directory's existence before writing to it, by using "os.makedirs(directory, exist_ok=True)" you can write the directory into existence and even if  it exists "exist_ok = True" will stop the terminal from throwing an error


**ATLAS: AML.T0010.001 + AML.T0010.003**
Under AML.T0010.001 + AML.T0010.003 the scanner should check if the directory it wants to write output file to exists because if tries to write to a nonexistent directory it can crashes or silently fail, this means the result of the scan is never logged so there is no refernce data once it comes time for auditing, hence the pipeline can't tell difference between "scan ran clean" or "scan never completed". This means that if the pipeline has been corrupted the scanner can't tell because ther is no forensic to prove that there was ever a scan.

### INJECTION 4
**Exact error:**
C:\Users\DELL\Documents\AdML_Lab\venv\Scripts\python.exe: No module named week_03_supply_chain_checker
'executable': 'C:\\Users\\DELL\\Documents\\AdML_Lab\\venv\\Scripts\\python.exe', 'platform': 'win32', 'in_venv': False, 'venv_path': None}, 'installed_packages_count': 1}, 'unpinned_deps': None, 'pickle_scan': {'risk_level': 'CLEAN', 'dangerous_count': 0, 'opcodes_found': [], 'file_found': True}, 'safe_to_proceed': False, 'warnings': ['You are currently trying to make use of pipeline outside the virtual environment'], 'timestamp': '2026-06-13T09:50:23.001865'}


**Exact fix:**
No fix is needed


**Causal WHY:**
The scanner is tested against the simulation "sys.prefix = sys.base_prefix" and the result is "in_venv = False" and "venv_path = None" this is because the scanner's logic is to return False and None when the virtual environment path is the same as global environment. Because in_venv is false safe_to_proceed is also False so the report will be a BLOCKED report. 



**Transferable principle:**
The scanner blocking an operation that has its virtual environment as a global environment is actually bad behavioural logic by scanner, as it is possible for the entire global environment to be a virtual environment so the scanner so always check rigorously if the user is in a virtual environment, this encompasses virtual within global and global-virtual.

**ATLAS: AML.T0010.001 + AML.T0010.003**
Under AML.T0010.001 + AML.T0010.003 the scanner should be able to differentiate between a virtual environment within a global environment and global_virtual environment, and a global environment, else it can lead operators to override the false positives using (--force) overrides or just flat ignoring the scanner, provided an unprotected global environment is ignored, an attacker can compromise the scanner by gaining control of an authorized user via phishing or execution of malicious code(most likely a reverse), and then executing malicious code in the pipeline thereby corrupting it. 

## June 2st, 2026 - WEEK 3 - MONDAY - dep_resolver.py
### REVIEW OF OUR CODE
The code we use a sort of cheat by calling import library, sys and calling function sys.path.insert(0, r'C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_2\src'), look at this function and the two arguments as a phone and two phone numbers, I can't do face to face communication cause we in different places so I just call you using the function sys.path.insert and the first argument, index 0 means me or current folder(my line), and the second argument is the folder we want to speak to be cohorts with so its the second phone and we communicate(the two argument) because of the phone(sys.path.insert)


g = Attackgraph is the way to call classes from a seperate script

we use the second argument within with open encoding = 'utf-8-sig' to read the file and convert BOM(Byte Order Mark)

Whenever we are looping a certain parameter and it can appear more than once we need to add break cause one is enough to be bad and it will overwrite mutiple times.

using try and except we can trigger a TimeoutError if the the subprocess.run exceeds timeout.

Just noticed the allowlist are only compared to the first element and the injection_chars is used throughout the lists, for the first element thing the entire list should be loop through for that so I added my own set and loop all elemts except the first.

Normally in an environment you would usually has a set of package dependencies that are allowed so when we parse the requirements file we validate the string of characters for op[0] and op[1] normally if in allow run if not block system

If a txt contains a package or packages with mutiple version it should block either the duplicate package or even better the entire file
### INJECTION 1
**Exact error:**
Traceback (most recent call last):
  File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\dep_resolver.py", line 70, in <module>
    print(parse_requirements('C:/Users/DELL/tmp/nonexistent.txt'))
          ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\dep_resolver.py", line 8, in parse_requirements
    raise FileNotFoundError(f"The file path {filepath} is not found")
FileNotFoundError: The file path C:/Users/DELL/tmp/nonexistent.txt is not found

**Exact fix:**
No fix needed

**Causal WHY:**
The script because the filepath that is to be executed doesn't exist, from the traceback the script triggered a condition that raised a FileNotFondError.

**Transferable principle:**
Every dependency checker should be able to verify the existence of the requirement filepath before checking for listed dependencies


**ATLAS:AML.T0010.001**
A dependency checker must validate the existence of a file path else the attacker can substitute the requirement file path with his corrupted version so he can install his malicious packages that tally with his requirement path which ships malicious code into our virtual environment. 


### INJECTION 2
**Exact error:**
{'': ['1.0.0'], 'numpy': ['1.24']}

**Exact fix:**
if not name:
  continue
if name:
  if name in pinned:
    pinned[name].append(package)
  else:
    pinned[name] = [package]
  break

**Causal WHY:**
The scripts runs and returns '' meaning empty, because the when we split using op we didn't check whether
name was empty or not before appending name and package to the list 

**Transferable principle:**
A proper dependency checker should be able to validate the dependency's name as non empty before returning the value as output

**ATLAS:AML.T0010.001**
If the dependency checker cannot validate an empty dependency name as a problem the attacker can use this logical flaw to bypass the dependency checker this can create or silent failure in ML pipeline


### INJECTION 3 
**Exact error:**
['numpy']

**Exact fix:**
No fix needed

**Causal WHY:**
The script returns numpy as the package name here because it is one with at least two versions. Because numpy has two version in the txt file, so when flag_duplicates in iterating over the dict and see's two values for the key numpy numpy is returned as the only package.

**Transferable principle:**
A dependency checker should be able to detect a package with multiple versions, because of the two, one with a higher version could have malicious payload embedded within it and that is one most likely to picked by pip.


**ATLAS:AML.T0010.001**
A dependency checker that detects a package with mutiple versions  should be able to block the file, else pip will most likely pick up the higher version to install which dangerous version leading to Alex Birsan Dependency attack or a reverse shell

### INJECTION 4
*Exact error:**
{'requests': ['2.31.0'], 'pytest': [None]}

**Exact fix:**
No fix needed

**Causal WHY:**
The dependency checker cuts out the bracket and string within it, returning package name pytest and [None] as the version, you can understand better by looking at the syntax for name = line.split(op)[0].split('[')[0] the job of split('[')[0] is to return strings before the squared bracket


**Transferable principle:**
A proper dependency checker should be able to strip away extra unecessary data such as [security] from pytest[security] and the return the package name in the requirement file, else it can cause the the checker to be corrupted especially when sorting through node downstream. 


**ATLAS:AML.T0010.001**
If the dependency checker can't strip away unnecessary data attached to checker, the attacker can use this attack surface to corrupt the topological_sort() of the nodes this creates a problem for the pipeline because bloat data is now circulating this reduce the pipeline's integrity.




## June 2st, 2026 - WEEK 3 - TUESDAY - safe_runner.py
### REVIEW OF CODE
We use subprocess and it used for system operation so its more modern than os library, allows you execute system commands and external applications, while shlex lets you split computer commands into strings

break it down for you, python uses subprocess.run to run shell scripts, cmd if it contains arg, then capture_output captures the outputs stdout and stderr which are the result where it worked or crashed, text returns captured as strings and timeout kills the process if it exceeds a time constaint that was set
### INJECTION 1
**Exact error:**
(venv) PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src> python -m week_03.safe_runner
Traceback (most recent call last):
  File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\safe_runner.py", line 36, in <module>
    print(safe_exec('python3 --version'))
          ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\safe_runner.py", line 17, in safe_exec
    raise TypeError("CMD IS NOT A LIST")
TypeError: CMD IS NOT A LIST

**Exact fix:**
No fix needed

**Causal WHY:**
The script crashed because the safe_exec is a function that only executes lists, from the traceback the script triggers a coniditon, where if cmd is not a list the script raises a TypeError

**Transferable principle:**
The safety checker is operating properly as it crashes and gives exact details crash(TypeError: CMD IS NOT A LIST), every good safety checker should be able to give reason for a failure so that the operator can log it and work on the issue.

**ATLAS: AML.T0010**
Under AML.T0010 every safety checker should be able to differentiate between certain data types at the function boundary before execution else the ML pipeline is compromised before model is ever loaded.

### INJECTION 2
**Exact error:**
venv) PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src> python -m week_03.safe_runner
Traceback (most recent call last):
  File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\safe_runner.py", line 36, in <module>
    print(safe_exec(['curl', 'https://x.com']))
          ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\safe_runner.py", line 19, in safe_exec
    raise ValueError(f"COMMAND {cmd[0]} IS NOT FOUND IN ALLOWED_COMMANDS ") 
ValueError: COMMAND curl IS NOT FOUND IN ALLOWED_COMMANDS


**Exact fix:**
no fix needed

**Causal WHY:**
The script executes the function safe_exec which contains an element that is not part of ALLOWED_COMMANDS, hence it triggers a coniditon of the script which raises a ValueError

**Transferable principle:**
The safety checker should be able to compare commands to the hardcoded allowlist, provided a command is not part of the allowlist block the command.

**ATLAS: AML.T0010**
An attacker that can execute unlisted commands like curl in the pipeline can fetch sensitive data such as source code or even execute occasional backdoor that can compromise the ML supply chain like SolarWind in 2020

### INJECTION 3 
**Exact error:**
Pre-Fix
(venv) PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src> python -m week_03.safe_runner
Traceback (most recent call last):
  File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\safe_runner.py", line 36, in <module>
    print(safe_exec(['python3', '-c', 'import os; os.system("id")']))       
          ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\safe_runner.py", line 21, in safe_exec
    raise ValueError("CMD ARGUMENTS ARE NOT ALLOWED")
ValueError: CMD ARGUMENTS ARE NOT ALLOWED

Post-Fix
(venv) PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src> python -m week_03.safe_runner
Traceback (most recent call last):
  File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\safe_runner.py", line 40, in <module>
    print(safe_exec(['python3', '-c', 'import os; os.system("id")']))       
          ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\safe_runner.py", line 23, in safe_exec
    raise ValueError(f"COMMAND {i} HAS FOUND IN DANGEROUS_FLAGS")
ValueError: COMMAND -c HAS FOUND IN DANGEROUS_FLAGS

**Exact fix:**
for i in cmd[1:]:
  if i in DANGEROUS_FLAGS:
    raise ValueError(f"COMMAND {i} HAS FOUND IN DANGEROUS_FLAGS")


**Causal WHY:**
We have to tracebacks, which proves our code was insufficient, the pre fix traceback is based on a certain string that is part of a excluded set, the post fix tells you one thing that python command can be rewritten to escape the excluded set from ['python3', '-c', 'import os; os.system("id")'] and ['python3', '-c', '__import__("os").system("id")'] look at it same same but different , so because of this issue we create an extra set that contains arguments that are blocked by the our fix's logic 
for i in cmd[1:]:
  if i in DANGEROUS_FLAGS:
    raise ValueError(f"COMMAND {i} HAS FOUND IN DANGEROUS_FLAGS")
 notice the fix loops through every element in the list after index zero because index zero is a command everything else is an argument

**Transferable principle:**
We must learn to validate commands, arguments as only validating commands is not enough as even permitted commands can have their own arguments utilised against them through flags

**ATLAS: AML.T0010**
An attacker that can take advantage of flags of trusted commands like python3 will be to fetch and access sensitive data from pipeline or even install their own malicious packages like Alex Birsan Dependecy attack


### INJECTION 4
**Exact error:**
PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src> python -m week_03.safe_runner
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\safe_runner.py", line 24, in safe_exec
    result = subprocess.run(cmd, capture_output = True, text =  True, timeout = timeout)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\subprocess.py", line 556, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\subprocess.py", line 1222, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
                     ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.3824.0_x64__qbz5n2kfra8p0\Lib\subprocess.py", line 1665, in _communicate
    raise TimeoutExpired(self.args, orig_timeout)
subprocess.TimeoutExpired: Command '['python3', '-c', '__import__("time").sleep(60)']' timed out after 2 seconds
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\safe_runner.py", line 37, in <module>
    safe_exec(['python3', '-c', '__import__("time").sleep(60)'], timeout=2)       
    ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^       
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\safe_runner.py", line 26, in safe_exec
    raise TimeoutError("Process exceeded Timeout")
TimeoutError: Process exceeded Timeout

**Exact fix:**
No fix needed

**Causal WHY:**
The script crashed because the command execution time exceeded the allowed time slot for operation, so it triggers the subprocess.TimeoutExpired thus raising a TimeoutError

**Transferable principle:**
Every safety checker must be able to restrict commands execution time to a threshold, else attacker can make use of this to stall the safety checker. 

**ATLAS: AML.T0010**
A safety checker that doesn't set a threshold for command execution is at risk of attacker using indefinite suspension of safety checker allowing the attacker to use the denial of service as dummy attack to buy time for main attacks like backdoor or dependency installation attack


## June 4st, 2026 - WEEK 3 - WEDNESDAY - supply_chain_checker.py (UPDATED)
### NOTICES
I noticed for the first injection the python version changed
### INJECTION 1
**Exact error:**
C:/Users/DELL/tmp/ghost.pkl doesn't exist
{'env_snapshot': {'python_info': {'version': '3.13.13', 'executable': 'C:\\Users\\DELL\\Documents\\AdML_Lab\\venv\\Scripts\\python.exe', 'platform': 'win32', 'in_venv': True, 'venv_path': 'C:\\Users\\DELL\\Documents\\AdML_Lab\\venv'}, 'installed_packages_count': 1}, 'unpinned_deps': None, 'pickle_scan': {'risk_level': 'MALICIOUS', 'dangerous_count': 0, 'opcodes_found': [], 'file_found': False}, 'safe_to_proceed': False, 'warnings': [], 'timestamp': '2026-06-11T10:34:19.001831'}

**Exact fix:**
No fix needed


**Causal WHY:**
From the output you can see that the file doesn't exist, and even at that the script doesn't crash because we use "try" and "except" to catch the error FileNotFoundError and prints "C:/Users/DELL/tmp/ghost.pkl doesn't exist" and thus the pre_flight_check is able to run. Then you can find the information "'file_found': False" within pickle_scan, the purpose of it is to trigger as True or False depending on the existence of the file in this case non existent means False is the read. Before the old code would print MALICIOUS based on the risk_level to block it making sure it wouldn't mislead the user because we never ran the file but we called it malicious, so adding file_found and changing triggers on the elif block would make sure we have no dead code. 



**Transferable principle:**
The problem of a non existent file triggering a MALICIOUS statement can often be misleading and these type of inconsistency can cause unwarranted alarms, this reduces integrity of the scanner.



**ATLAS: AML.T0010.001 + AML.T0010.003**
Under AML.T0010.001 + AML.T0010.003 a scanner that labels both "non existent file" and a "malicious file" detection the same way trains operators to ignore or distrust MALICIOUS alerts, so when a real compromised file reaches the checkpoint it might get dismissed as a false positive

### INJECTION 2
**Exact error:**
Traceback (most recent call last):
  File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\supply_chain_checker.py", line 53, in <module>
    print(pre_flight_check('/tmp/benign.pkl', '/tmp/no_such_req.txt'))
          ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\supply_chain_checker.py", line 11, in pre_flight_check
    unpinned = flag_unpinned(requirements_path)
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\env_auditor.py", line 33, in
 flag_unpinned
    raise FileNotFoundError(f"Requiremnts file path not found {requirements_path}")
FileNotFoundError: Requiremnts file path not found /tmp/no_such_req.txt


**Exact fix:**
try:
  parsed = parse_requirements(requirements_path)
  unpinned = dep_flag_unpinned(parsed)
except FileNotFoundError as e:
  unpinned = None
  warnings.append("The requirement path can't be found")


**Causal WHY:**
The pre_flight_check tries to access a path using the flag_unpinned function and since it the check os.path.exists() and its False it raises a FileNotFoundError using the hardcoded instruction within the if the block from flag_unpinned function in env_auditor.py




**Transferable principle:**
A proper scanner should block operations where certain requirements are not met in other to protect the intergrity of our pipeline. Because if we have a silent crash this will lead to an incomplete report effectively(in the long run) corrupting our pipeline.



**ATLAS: AML.T0010.001 + AML.T0010.003**
Under AML.T0010.001 + AML.T0010.003 the scanner should be able to block operation when the dependency file doesn't exist because in ML supply chains when a scanner doesn't check for requirement file or silently fails it that is a vunerablilty because the attacker  and a threat actor will be able to install his malicious dependencies on the victim's system like Alex Birsan PyPI dependency attack. But the problem is because the script crashed and did not send a blocked report or a report at all there is no record to investigate.

### INJECTION 3
**Exact error:**
SAFE TO PROCEED
{'env_snapshot': {'python_info': {'version': '3.13.14', 'executable': 'C:\\Users\\DELL\\Documents\\AdML_Lab\\venv\\Scripts\\python.exe', 'platform': 'win32', 'in_venv': True, 'venv_path': 'C:\\Users\\DELL\\Documents\\AdML_Lab\\venv'}, 'installed_packages_count': 1}, 'unpinned_deps': None, 'pickle_scan': {'risk_level': 'CLEAN', 'dangerous_count': 0, 'opcodes_found': [], 'file_found': True}, 'safe_to_proceed': True, 'warnings': [], 'timestamp': '2026-06-12T15:31:07.735049'}

**Exact fix:**
No fix is needed



**Causal WHY:**
The scanner is tested against "shutil.rmtree('output', ignore_errors = True)" and the directory file still gets created because we added a safeguard "os.makedirs(os.path.dirname(output_path), exist_ok = True)" that ensures that even if directory doesn't exist it will be created hence the function pre_check still produces the .json log file.


**Transferable principle:**
A script that writes output files should never assume that it's target directory exists, it should always check for the directory's existence before writing to it, by using "os.makedirs(directory, exist_ok=True)" you can write the directory into existence and even if  it exists "exist_ok = True" will stop the terminal from throwing an error


**ATLAS: AML.T0010.001 + AML.T0010.003**
Under AML.T0010.001 + AML.T0010.003 the scanner should check if the directory it wants to write output file to exists because if tries to write to a nonexistent directory it can crashes or silently fail, this means the result of the scan is never logged so there is no refernce data once it comes time for auditing, hence the pipeline can't tell difference between "scan ran clean" or "scan never completed". This means that if the pipeline has been corrupted the scanner can't tell because ther is no forensic to prove that there was ever a scan.

### INJECTION 4
**Exact error:**
C:\Users\DELL\Documents\AdML_Lab\venv\Scripts\python.exe: No module named week_03_supply_chain_checker
'executable': 'C:\\Users\\DELL\\Documents\\AdML_Lab\\venv\\Scripts\\python.exe', 'platform': 'win32', 'in_venv': False, 'venv_path': None}, 'installed_packages_count': 1}, 'unpinned_deps': None, 'pickle_scan': {'risk_level': 'CLEAN', 'dangerous_count': 0, 'opcodes_found': [], 'file_found': True}, 'safe_to_proceed': False, 'warnings': ['You are currently trying to make use of pipeline outside the virtual environment'], 'timestamp': '2026-06-13T09:50:23.001865'}


**Exact fix:**
No fix is needed


**Causal WHY:**
The scanner is tested against the simulation "sys.prefix = sys.base_prefix" and the result is "in_venv = False" and "venv_path = None" this is because the scanner's logic is to return False and None when the virtual environment path is the same as global environment. Because in_venv is false safe_to_proceed is also False so the report will be a BLOCKED report. 



**Transferable principle:**
The scanner blocking an operation that has its virtual environment as a global environment is actually bad behavioural logic by scanner, as it is possible for the entire global environment to be a virtual environment so the scanner so always check rigorously if the user is in a virtual environment, this encompasses virtual within global and global-virtual.

**ATLAS: AML.T0010.001 + AML.T0010.003**
Under AML.T0010.001 + AML.T0010.003 the scanner should be able to differentiate between a virtual environment within a global environment and global_virtual environment, and a global environment, else it can lead operators to override the false positives using (--force) overrides or just flat ignoring the scanner, provided an unprotected global environment is ignored, an attacker can compromise the scanner by gaining control of an authorized user via phishing or execution of malicious code(most likely a reverse), and then executing malicious code in the pipeline thereby corrupting it.

## June 4st, 2026 - WEEK 3 - THURSDAY SELF-ASSESSMENT 
### SELF ASSESSMENT
**model_loader.py quality(1-5 + justification):**
3/5
I understand Opcode scanning, cause we concluded that byte to byte scanning make the scanner to rigourous so we employed opcode positioning via pickletools.dis(). We removed APPEND from DANGEROUS_OPCODES because its a false positive,  because its not dangerous alone unless paired with opcodes like "GLOBAL" or "REDUCE".

**env_auditor.py quality (1-5 + justification):**
4/5
I understand the environment scanning, get_python_info, get_installed_packages, write_snapshot, these functions a do solid job but flag_unpinned isn't capable of scraping extra data like comments and blank lines from the txt file.

**supply_chain_checker.py quality (1-5 + justification):**
3/5
I understand how pre_flight_check incorporated mutiple functions to build a function that scans the model and the surrounding and software dependcies of the system or environment, and run_and_save uses the data from the scan in pre_check to detect safety of the operation. But flag_unpinned from the env_auditor was replaced by flag_unpinned and parse_requirement from dep_solver.

**dep_resolver.py quality (1-5 + justification):**
4/5
I understand the function parse_requirement how it extracts the data from the text files and turn it to dict, flag_unpinned extract keys without values dict, flag_duplicates extract keys with mutiple values from the dict, build_dep_graph makes use of Class Attackgraph from attackgraph to sort out the nodes(packages). Although parse_requirements fails to check for filepath existence before trying to execute it.

**safe_runner.py quality (1-5 + justification):**
4/5
The functions shell_injection_check, safe_exec, and run_python_script, all work correctly, type validation, allowlist enforcement, injection detection and timeout handling, passing all the 4 injections. The main weakness is my arg fix is producing false positive.

**log.md quality (1-5 + justification):**
3/5
The log documentation shows the techincal prowess(via the change of logic to make the scanner more rigorous) and understanding of the injections provided. But this was affected by the choice of words and underexplanation of some instances

**What I would do differently if Week 3 started again:**
I would have completed each day's session on the scheduled day instead of procastinating and distracting myself with filler content like 5 year plan lookups and surfing on websites that are for week 20 forward just salivating at the reward without putting the commits working .

**What the pickle scanner taught me about loading weights in Month 2:**
In month 2 torch.load() will be about code execution not file reading, so using our pickle scanner we are trying to protect our environment cause else our pipeline up till month 2 is at risk or attack


**What safe_runner taught me about subprocess security in agentic systems:**
When engaging agentic system workflows, it is very important to remember that agentic workflows are usually automated so it is important to infuse timeout handling feature within the workflows so that the workflow can continue automation in the case of a stalled or hanging processes, and the workflow must always validate inputs first before they hit subprocess.










































