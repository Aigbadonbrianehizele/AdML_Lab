import sys
def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "/":
        return a / b
    else:
        return None
a = sys.argv[1]
b = sys.argv[2]
result = calculate(a, b, sys.argv[3])
print(result)              