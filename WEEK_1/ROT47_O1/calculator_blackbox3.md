## [Thursday] Week 1 — CVE-2021-37678 Class — calculator_blackbox.py

---

### Injection 1: Basic Addition
**What I was trying to do:I was tryna add 5 and 3**
**What broke: python calculator_blackbox3.py 5 3 +
53**
**Why it broke: sys.argv defaults characters as strings cause OS reads them as tokens, C reads them as strings and pythonWe define the paramters a and b as int by enclosing the sys.argv index with int() follows C**
**How I fixed it: I wrapped sys.argv[1] and sys.argv[2] with float() function. float() converts them from string or strings to float numbers capable of arithmetic operations python calculator_blackbox3.py 5 3 +
8
a = float(sys.argv[1])
b = float(sys.argv[2])**
**What I learned: I learned that we have to wrap our inputs and not assume that will always be read as interger or float numbers**
**MITRE ATLAS:** AML.T0043 —

---

### Injection 2: Division by Zero
**What I was trying to do: I was trying to divide 10 by 0**
**What broke:PS C:\Users\DELL\Documents\ROT47> python calculator_blackbox3.py 10 0 /
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\ROT47\calculator_blackbox3.py", line 11, in <module>
    result = calculate(a, b, sys.argv[3])
  File "C:\Users\DELL\Documents\ROT47\calculator_blackbox3.py", line 6, in calculate
    return a / b
           ~~^~~
ZeroDivisionError: division by zero**
**Why it broke: The program ran into a ZeroDivisionError because the input b is zero **
**How I fixed it:I added a new line of code using an if statement stating that if b equals 0 print error please error using sys.exit() function
 if b == 0:
        sys.exit("Error: Please Error") **
**What I learned:We need to think of each and evry possible situation possible when making a calculator**
**MITRE ATLAS:** AML.T0043 —

---

### Injection 3: Unknown Operator
**What I was trying to do:*I trying to do modulus operation of 10 and 3*
**What broke:PS C:\Users\DELL\Documents\ROT47> python calculator_blackbox3.py 10 3 %
None**
**Why it broke:Because % is not defined as one of the op possible inputs**
**How I fixed it:I added % as a possible operator using an if statement
if op == "%":
        return a % b 
**
**What I learned:I learned that before performing an operation we should check if it part of the possible inputs**
**MITRE ATLAS:** AML.T0043 —

---

### Injection 4: No Arguments
**What I was trying to do: I just tried to call the code noramlly **
**What broke:PS C:\Users\DELL\Documents\ROT47> python calculator_blackbox3.py
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\ROT47\calculator_blackbox3.py", line 13, in <module>
    a = float(sys.argv[1])
              ~~~~~~~~^^^
IndexError: list index out of range**
**Why it broke: sys.argv expects indexes 1, 2, 3 to exist and since they are not called it breaks and cause and IndexError**
**How I fixed it:I fixed by adding an if statement that dictates if length of sys.argv function is not 4 print rror: not enough inputs *
**What I learned:When dealing with sys.argv always call your the index in the command line
python calculator_blackbox3.py 10 3 %
1.0**
**MITRE ATLAS:** AML.T0043 —

---

### Injection 5: Type Confusion
**What I was trying to do:I was trying to add a abc to 3**
**What broke: C:\Users\DELL\Documents\ROT47> python calculator_blackbox3.py abc 3 +
Traceback (most recent call last):
  File "C:\Users\DELL\Documents\ROT47\calculator_blackbox3.py", line 13, in <module>
    a = float(sys.argv[1])
ValueError: could not convert string to float: 'abc'**
**Why it broke: abc is a string of characters and it cannot be converted to a float**
**How I fixed it:I added a try and except statement, so I defined inputs a and b within the try statement and defined a sys.exit function that prints Error this data type is not allowed if the string can't be converted to a float **
**What I learned:Pay close attention to your inputs**
**MITRE ATLAS:** AML.T0043 —