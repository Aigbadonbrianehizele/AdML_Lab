# Break-Fix Log

Trainee: Brian (Lagos, NG)  
Program: AI Red Team Master Log  
Week: 1 - Black Box Exercise

---

## Entry Template (Copy for each issue)

### Entry 1: No return command(TypeError)

**Date:** 2026-04-05  
**Week:** 1  
**ATLAS Technique:** AML.T0000

#### OBSERVE: I legit wrote the equation 5 + 3 in and nothing happened 
```
> 5 + 3

```

#### EXPECT: I expected nothing
```
I expected nothing to happen 
```

#### ISOLATE: Simplest Reproduction
```
-c means command
python -c "from calculator_blackbox import add; print(add(5, 3))"
```

#### HYPOTHESIZE: No return statement or print statement for result
1. There is no return statement or print statement 
2. Definitely no return statement
3. It returns none
#### TEST: Verification
```python 
we added a temporary print statement and replaced the result with return statement to debug the the funtion this addition made to the add function

print(f"DEBUG: a is {type(a)} and b is {type(b)}")
return a + b
''' this the result
BLACK BOX CALCULATOR
========================================
Enter calculations like: 5 + 3
Type 'quit' to exit
========================================

> 5 + 3
DEBUG: a is <class 'str'> and b is <class 'str'>
Result: 53
```

#### ROOT CAUSE: The Actual Problem
```
there was no return statement andthere is a problem where the characters are being defined as strings
```

#### THE FIX
```python
def add(a, b):
    """Add two numbers"""
    return  a + b
"""for the add fuction
for the parts we do 
"""a = float(parts[0])  # Should this be converted?
    operator =(parts[1])
    b = float(parts[2])  # Should this be converted?
```

#### VERIFICATION
```
PS C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (3)\week1_blackbox\src\week_01> python calculator_blackbox.py
========================================
BLACK BOX CALCULATOR
========================================
Enter calculations like: 5 + 3
Type 'quit' to exit
========================================

> 5 + 3
Result: 8.0
```

#### LESSON LEARNED
```
Umm I learned than expression.split() assumes str and we have to make modifications ourselves and  I also learned that the debugging isn't what I taught it would be, I learnt that more command line syntax and more python syntaxes
```

---

## Entry 2: wrong command after the return statement for subtract and split() takes data and read them as str instead of int or float

**Date:*2026-04-05*  
**Week:** 1  
**ATLAS Technique:** AML.T0000

#### OBSERVE: After I hit ran the equation 10 - 2 I got 102
```
1. I suspect that there is add sign instead of subtract and the data is being read as characters(strings) instead of integers

```

#### EXPECT: Lowkey expected to see 8, but I am debugging
```
Got the wrong value which was 102 instead of 8
```

#### ISOLATE: Simplest Reproduction
```python -c "from calculator_blackbox import subtract ; print(subtract(10, 2))"
12
```

#### HYPOTHESIZE: Wrong sign and wrong data representation confirmed
1. As I suspected subtract is making use of addition sign in the return statement
2. What more is that last time I got 102 and after minimal reproduction I go 12 meaning that there is it is confirmed that the parts = expression.split() is reading str
3. 

#### TEST: Verification
```
BLACK BOX CALCULATOR
========================================
Enter calculations like: 5 + 3
Type 'quit' to exit
========================================

> 10 - 2
DEBUG: a is <class 'float'> and b is <class 'float'>
Result: 8.0
So we change the statement after return from a + b to a - b and we add a print statement before return statement to debug and adding float to parts 

print(f"DEBUG: a is {type(a)} and b is {type(b)}")
10 - 2
DEBUG: a is <class 'str'> and b is <class 'str'>
Result: 102
 
   
```

#### ROOT CAUSE: The Actual Problem
```
There are two problem first the sign for add was used for subtract function in the return statement and second the the parts automactically defines any character as a string and because of that all of our data will be read as strings and we need a and b to be read as integers or floats and then we add float to a and b 
```

#### THE FIX
```python
 return a - b
 a = float(parts[0])  
 b = float(parts[2]) 

```

#### VERIFICATION
```
Ran it in interactive mode an got 10 - 2 equals 8
```

#### LESSON LEARNED
```
Always verify the data types properly especially when you calling the character one by one like when parts is used
```

---

## Entry 3: The return statement a is being defined as a string and two different data types won't work so we must changed a back to an integer

**Date:*2026-04-05*  
**Week:** 1  
**ATLAS Technique:** AML.T0000

#### OBSERVE: When I tried to add the equation  4*5 obviouly I expected to see 20 but then I got a file error
```
PS C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (3)\week1_blackbox\src\week_01> python calculator_blackbox.py
========================================
BLACK BOX CALCULATOR
========================================
Enter calculations like: 5 + 3
Type 'quit' to exit
========================================

> 4 * 5
Traceback (most recent call last):
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (3)\week1_blackbox\src\week_01\calculator_blackbox.py", line 117, in <module>
    interactive_mode()
    ~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (3)\week1_blackbox\src\week_01\calculator_blackbox.py", line 76, in interactive_mode
    result = calculate(user_input)
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (3)\week1_blackbox\src\week_01\calculator_blackbox.py", line 54, in calculate
    return multiply(a, b)
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (3)\week1_blackbox\src\week_01\calculator_blackbox.py", line 31, in multiply
    return str(a) * b  # This seems odd
           ~~~~~~~^~~
TypeError: can't multiply sequence by non-int of type 'str'

```

#### EXPECT: I expected to see result as 20
```

```

#### ISOLATE: Simplest Reproduction
```python -c "from calculator_blackbox import multiply ; print(multiply(4, 5))"
you get 44444

```

#### HYPOTHESIZE: Possible Causes
1. 4 is being processed as a string instead of an integer
2. So this is obviously a type error issue
3. TypeError: can't multiply sequence by non-int of type 'str' the minimal reproduction

#### TEST: Verification
```python
print(f"DEBUG: a is {type(a)} and b is {type(b)}")
PS C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01> python calculator_blackbox2.py
========================================
BLACK BOX CALCULATOR
========================================
Enter calculations like: 5 + 3
Type 'quit' to exit
========================================

> 4 * 5
DEBUG: a is <class 'str'> and b is <class 'str'>
Traceback (most recent call last):
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01\calculator_blackbox2.py", line 119, in <module>
    interactive_mode()
    ~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01\calculator_blackbox2.py", line 78, in interactive_mode
    result = calculate(user_input)
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01\calculator_blackbox2.py", line 56, in calculate
    return multiply(a, b)
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01\calculator_blackbox2.py", line 33, in multiply
    return str(a) * b  # This seems odd
           ~~~~~~~^~~
TypeError: can't multiply sequence by non-int of type 'str'
```

#### ROOT CAUSE: The Actual Problem
```
The line contains return str(a) * b
so when we do mininmal reproduction since we see 44444 it means the minimal reprduction makes b an integer and when we run the code normally we get TypeError: can't multiply sequence by non-int of type 'str'meaning b is getting read as str using the original interface
```

#### THE FIX
```return a * b
   a = float(parts[0]) 
   b = float(parts[2])

```

#### VERIFICATION
```
> 4 * 5
Result: 20.0
```

#### LESSON LEARNED
```
I learned that we should check how the character in classified in terms of data type.
```

---


---

## Entry 4: ZeroDivisionerror

**Date:*2026-04-05*  
**Week:** 1  
**ATLAS Technique:** AML.T0000

#### OBSERVE: When I divided by zero I didn't get a feedback usually meaning there is all conditions where not specified and it means that instance was not accounted for
```

```

#### EXPECT: I expected to error or not possible
```

```

#### ISOLATE: Simplest Reproduction
```python -c "from calculator_blackbox import divide ; print(divide(5, 0))"

```

#### HYPOTHESIZE: Possible Causes
1. The code doesn't have feedback for zero division
2. That's pretty much the only problem
3. 

#### TEST: Verification
```python
print(f"DEBUG: a is {type(a)} and {type(a)}")
PS C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01> python calculator_blackbox2.py
========================================
BLACK BOX CALCULATOR
========================================
Enter calculations like: 5 + 3
Type 'quit' to exit
========================================

> 5 / 0
DEBUG: a is <class 'str'> and <class 'str'>
Traceback (most recent call last):
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01\calculator_blackbox2.py", line 120, in <module>
    interactive_mode()
    ~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01\calculator_blackbox2.py", line 79, in interactive_mode
    result = calculate(user_input)
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01\calculator_blackbox2.py", line 59, in calculate
    return divide(a, b)
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01\calculator_blackbox2.py", line 38, in divide
    return a / b  # What if b is 0?
           ~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'str'
PS C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01> 
```

#### THE FIX
```add
if b == 0:
            return None
also add            
else:
   print("ERROR")

```

#### VERIFICATION
```
PS C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (3)\week1_blackbox\src\week_01> python calculator_blackbox.py
========================================
BLACK BOX CALCULATOR
========================================
Enter calculations like: 5 + 3
Type 'quit' to exit
========================================

> 5 / 0
error
```

#### LESSON LEARNED
```
Alway make sure to the final input for the code 
```

---
---

## Entry 5: We ran into an invalid error

**Date:** 20226-04-05
**Week:** 1  
**ATLAS Technique:** AML.T0000

#### OBSERVE: I lowkey expected error and guess what I saw was blanks bro
```

```

#### EXPECT: I expected error 
```

```

#### ISOLATE: Simplest Reproduction
```python -c "from calculator_blackbox import add ; print(add(abc, 3))"
PS C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01> python -c "from calculator_blackbox2 import add; print(add(abc, 3))"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    from calculator_blackbox2 import add; print(add(abc, 3))
                                                    ^^^
NameError: name 'abc' is not defined. Did you mean: 'abs'? Or did you forget to import 'abc'?

```

#### HYPOTHESIZE: Possible Causes
1. Obviuosly it is a nameError
2. Well probably cause the python sees abc as a variable that is undefined
3. 

#### TEST: Verification
```python 
print(f"DEBUG: a is {type(a)} and {type(a)}")
PS C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01> python calculator_blackbox2.py
========================================
BLACK BOX CALCULATOR
========================================
Enter calculations like: 5 + 3
Type 'quit' to exit
========================================

> abc + 3
DEBUG: a is <class 'str'> and <class 'str'>

> Traceback (most recent call last):
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01\calculator_blackbox2.py", line 121, in <module>
    interactive_mode()
    ~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01\calculator_blackbox2.py", line 75, in interactive_mode
    user_input = input("> ")
KeyboardInterrupt
```

#### ROOT CAUSE: The Actual Problem
```
The string abc is undefined so it will give nameerror
```

#### THE FIX
```python
   if len(parts) != 3:
        print("Invalid expression format")
        return None
    try:
        a = parts[0]  # Should this be converted?
        operator = parts[1]
        b = parts[2]  # Should this be converted?
    except ValueError:
        return "error"

```

#### VERIFICATION
```
PS C:\Users\DELL\Downloads\Kimi_Agent_Path to Elite Red Team (4)\week1_blackbox\src\week_01> python calculator_blackbox2.py
========================================
BLACK BOX CALCULATOR
========================================
Enter calculations like: 5 + 3
Type 'quit' to exit
========================================

> abc + 3
Result: error
```
#### LESSON LEARNED
```
Always check the to make sure the data type OR characters you fill in.
```



---

## Summary Table

| Entry | Issue | Type | Fixed? |
|-------|-------|------|--------|
| 1 | [name] | [crash/wrong/silent] | [Y/N] |
| 2 | [name] | [crash/wrong/silent] | [Y/N] |
| 3 | [name] | [crash/wrong/silent] | [Y/N] |
| 4 | [name] | [crash/wrong/silent] | [Y/N] |
| 5 | [name] | [crash/wrong/silent] | [Y/N] |

---

## Blockers (Issues You Couldn't Solve)

| Issue | Why Blocked | Plan to Unblock |
|-------|-------------|-----------------|
| | | |

---

## Time Tracking

| Activity | Time Spent |
|----------|------------|
| Initial exploration | |
| Issue 1 | |
| Issue 2 | |
| Issue 3 | |
| Issue 4 | |
| Issue 5 | |
| Documentation | |
| **Total** | |
