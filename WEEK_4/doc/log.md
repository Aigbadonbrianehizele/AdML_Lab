## [Week 4 / Monday] Broadcasting failure — case 1: leading axis mismatch
**Code:**
a = np.random.randn(4, 3, 32, 32)
b = np.random.randn(5, 32, 32)
result = a + b

**Exact output (verbatim):**
ValueError: operands could not be broadcast together with shapes (4,3,32,32) (5,32,32) 

**Causal WHY:**
If you notice one of the two shapes an column breaks the conditions of broadcasting
               (4, 3, 32, 32)
               (   5, 32, 32)
if you notice the third column from the right (since the broadcasting is right alignment focused) it violates the conditions of broacasting
Conditions of Broadcasting
1. In a each column broadcasting is possible if values are the same or one of the values is equal to 1(stretch).
2. For a column on the left most side(pay attention to left most) if the one of the columns is empty it has the same effect as the empty space being a value of 1 it will stretch 

Our code violates condition number 1 the third column where the values are 3 and 5 hence the traceback


## [Week 4 / Monday] Broadcasting failure — case 2: Middle axis mismatch
**Code:**
a = np.random.randn(4, 3, 32, 32)
b = np.random.randn(3, 12, 32)
result = a + b
**Exact output (verbatim):**
ValueError: operands could not be broadcast together with shapes (4,3,32,32) (3,12,32) 
**Causal WHY:**
               (4, 3, 32, 32)
               (   3, 12, 32)
If you notice the shape one of the axis doesn't obey the conditions that is the middle axis it violates condition number 1 comparing 32 and 12

## [Week 4 / Monday] Broadcasting failure — case 3: Two axis mismatch
**Code:**
a = np.random.randn(4, 3, 32, 32)
b = np.random.randn(5,7,32,32)
result = a + b
**Exact output (verbatim):**
ValueError: operands could not be broadcast together with shapes (4,3,32,32) (5,7,32,32)

**Causal WHY:**
(4, 3, 32, 32)
(5, 7, 32, 32)
Actually here two axis the axis zero and the second axis both violate the condition number 1 comparing 4 to 5, 3,7

