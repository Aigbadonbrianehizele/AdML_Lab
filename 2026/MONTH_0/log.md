## May 31st, 2026 - WEEK 3 - SAT PART 1 - model_loader.py


### Injection 1

**Exact error:**
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\model_loader.py", line 43, in <module>
    print(scan_pickle('C:/Users/DELL/tmp/does_not_exist.pkl'))
          ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\model_loader.py", line 15, in scan_pickle
    raise FileNotFoundError
FileNotFoundError

**Exact Fix:**
if not os.path.exists(filepath):
        raise FileNotFoundError

So the file line of the fix os.path.exists() is a special method that checks for existence so paired with if not, it means if file path doesn't exist, from line 2 raise a FileNotFoundError

**Casual WHY:**
When os make makes the syscall to the physical memory if the filepath doesn't exist, python will raise a FileNotFoundError

**Transferable principle:**
Before a script can be executed, the file path must exist(full file validattion). 

**ATLAS: AML.T0010**
A pre-flight scanner that crashes on invalid input doesn't justify the file as malicious content.


### Injection 2
**Exact error:**
PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03> python model_loader.py
{'filepath': 'C:/Users/DELL/tmp/empty.pkl', 'file_size_bytes': 0, 'opcodes_found': [], 'dangerous_count': 0, 'risk_level': 'CLEAN', 'safe_to_load': True}

**Exact fix:**
if os.path.getsize(filepath) == 0:
    raise ValueError


**Casual WHY:**
An empty file contains no opcodes hence dangerous_count returns 0, since dangerous count is 0 risk_level returns CLEAN, and then the safe_to_load returns True because risk_level returns CLEAN.

**Transferable principle:**
Our pre flight scanner should be able to discern between and empty file and a file with size that's like loading empty bottle for shipment when it has no content it's just waste.

**ATLAS: AML.T0010**
A pre filght scanner that accepts an empty file(pytorch model) it risks reducing the accuracy of the ML supply chain or environment

 

### Injection 3
**Exact error:**
PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03> python model_loader.py
[{'opcode': 'INST', 'offset': 2}, {'opcode': 'INST', 'offset': 5}, {'opcode': 'APPENDS', 'offset': 14}]

**Exact fix:**
No fix needed here.

**Casual WHY:**
Because some of the letters trigger the scan_pickle() method which filters out dangerous opcodes , so its aggressive because it searches byte by byte


**Transferable principle:**
The pre flight scanner works a bit too well cause if looks at meaningful sentences like the example we wrote into the file and it calls some bytes out as dangerous

**ATLAS: AML.T0010**
Because of pre flight scanner to aggressive("works to well") it will often lead to many false positives and these reduces the accuracy of the ML supply chain or environment



### Injection 4
**Exact error:**
Output: 5518 dangerous opcodes found, risk_level: MALICIOUS, safe_to_load: False
Scanner did not crash. Full output truncated — 5518 entries.
**Exact fix:**
No fix needed
**Casual WHY:**
The function audit_report() method is used to police through the entire file byte by byte for the joined values like 9934 it will shred it to single byte and police through it and because the sample space is 100k intergers we get a dangerous_count is 5518
**Transferable principle:**
This large result shows us that our scanner is trustworthy enough to check through large model
**ATLAS: AML.T0010**
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
  raise FileNotFoundError(f"Requiremnts file path not found {requirements_path}")


**Casual WHY:**
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

**Casual WHY:**
The flag_unpinned to returns an empty container [] solely because the file in the path is empty

**Transferable principle:** A pre flight scanner should be able to return an empty container if the file being read is empty, rather than silently crash as this affect our ML supply chain

**ATLAS: AML.T0010**
When flag_unpinned returns an empty container [] it means there are unpinned dependencies which go undetected leaving the ML pipeline open to dependency confusion attacks similar to Alex Birsan 2020

### Injection 3
**Exact error:**
['pytest']

**Exact fix:**
no fix needed
**Casual WHY:**
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


**Casual WHY:**
The reason why we have no error is because "exist_ok = True" stops the FileExistsError when you are trying to create a directory that already exists and it help to create a directory that doesn't exist so it also stops FileNotFoundError 

**Transferable principle:**
A pre filight scanner must be able to store all the contents of its last check in a particular path and if that path doesn't exist employ "os.makedirs" and 'exist_ok = True" to create a path to store the final information on the check


**ATLAS: AML.T0010**
A pre flight scanner must be capable of storing data taken during check in a file so that the data can be cross refernced with the next check, overwriting of previous data or deletion of content will make it harder to track safety of the virtual environment puttinhg the ML supply chain at risk of silent corruption by threat actors








