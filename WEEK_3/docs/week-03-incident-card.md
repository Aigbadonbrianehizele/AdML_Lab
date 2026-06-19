# Incident Card — Week 3

## Finding 001 — Hugging Face Class: Malicious Pickle Payload

**Real-world class:** 
Hugging Face Malicious Model Uploads (2024)

**Severity:** 
Critical

**Description:**   
Scan_pickle() did not validate files existence or handle empty file before attempting to read bytes, causing the missing file raised a FileNotFoundError and audit_report made an empty file actually crash and return a ValueError in the traceback because the an empty file is a zero-byte file because scan_pickle also failed to validate file size

**Proof of Concept:** 
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\model_loader.py", line 43, in <module>
    print(scan_pickle('C:/Users/DELL/tmp/does_not_exist.pkl'))
          ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\model_loader.py", line 15, in scan_pickle
FileNotFoundError

(venv) PS C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03> python model_loader.py
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\model_loader.py", line 48, in <module>
    print(audit_report('/tmp/empty.pkl'))
          ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\model_loader.py", line 35, in audit_report
    audit = scan_pickle(filepath)
  File "C:\Users\DELL\Documents\AdML_Lab\2026\MONTH_0\WEEK_3\src\week_03\model_loader.py", line 18, in scan_pickle
ValueError

**Root Cause:** 
scan_pickle was written to handle valid files only, input validation was never considered initially during the build leaving the function vulnerable to edge cases such as missing files and empty files at the entry point

**Fix Applied:** 
if not os.path.exists(filepath):
    raise FileNotFoundError
if os.path.getsize(filepath) == 0:
    raise ValueError

**Residual Risk:** 
scan_pickle doesn't validate the file as an actual pickle stream before scanning, a non pickle file will cause an error during opcode scanning and file permission errors are unhandled also causing the script to crash


**ATLAS:** AML.T0010.001 + AML.T0010.003
Under AML.T0010.001 + AML.T0010.003 an attacker can upload unvalidated file types that bypass the defence of the scanner by causing it to crash, meaning the attacker has bypassed the scanner giving way for executing malicious pickle streams using pickle.load().
## Finding 002 — SolarWinds Class: Environment Fingerprinting Bypass

**Real-world class:** 
SolarWinds SUNBURST (2020)

**Severity:** 
Critical

**Description:** 
flag_unpinned doesn't validate the file's existence before trying to read it result read the file line by line causing the missing file to crash and report a FileNotFoundError
**Proof of Concept:** 
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

**Root Cause:** 
Flag_unpinned() is written to handle valid file paths only, input validation wasn't part of the implementation in the initial phases leaving enough room for a case such as missing files.

**Fix Applied:** 
if not os.path.exists(requirements_path):
  raise FileNotFoundError(f"Requirements file path not found {requirements_path}")

**Residual Risk:** 
flag_unpinned doesn't handle file permission errors causing the function to crash, malformed lines aren't properly parsed so redundant data will be parsed into logs corrupting the data.

**ATLAS:** AML.T0010.001
Under AML.T0010.001 an attacker can upload a file with the wrong permission(no read) causing the scanner to crash, enabling the attacker to manipulate the build environment state by parsing requirement files that contain malicious unpinned dependencies that go undetected. 



## Finding 003 — CodeCov Class: Silent Integration Failure
**Real-world class:**
 CodeCov Bash Uploader Compromise (2021)

**Severity:** 
Critical

**Description:** 
pre_flight_check() fails to validate the existence of the external dependency file before trying to read it, result in FileNotFoundError being raised

**Proof of Concept:** 
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

**Root Cause:** 
pre_flight_check() is built to handle files whose existence have been validated, so input validation wasn't considered earlier during build phase.

**Fix Applied:**
 try:
   unpinned = flag_unpinned(requirements_path)
except FileNotFoundError as e:
  unpinned =  None
  warnings.append("The requirement path can't be found") 

**Residual Risk:**
pre_flight_check doesn't handle file permission causing function to crash, malformed lines aren't properly sanitized meaning there that redundant data will be stored in logs, it doesn't also handle file type validation for pickle files, meaning non pickle files will cause the function to crash.

**ATLAS:** AML.T0010.001 + AML.T0010.003
Under AML.T0010.001 + AML.T0010.003 an attacker can upload file without read permission causing the scanner to crash, after then bypassing the scanner and uploading malicious pickle model, the model scanner never runs because of the crash meaning there is no forensic data for operators to sort through.
