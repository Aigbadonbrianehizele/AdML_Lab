# calculator_blackbox.py
# Week 1: Black Box Exercise
# 
# INSTRUCTIONS:
# 1. Run this file: python calculator_blackbox.py
# 2. Test various inputs (try: 5 + 3, 10 - 2, 4 * 5, 8 / 0, etc.)
# 3. Document any unexpected behavior in logs/breakfix.md
# 4. DO NOT READ THE CODE YET - treat it as a black box
# 5. Only look at the code after you've documented 3+ issues
#
# HINT: There are 5 issues total. Some are obvious, some are subtle.

import sys

def get_number(prompt):
    """Get a number from user input"""
    value = input(prompt)
    return value  # TODO: Is this right?

def add(a, b):
    """Add two numbers"""
    return  a + b
    # Is something missing here?

def subtract(a, b):
    """Subtract b from a"""
    return a - b  # Double check this

def multiply(a, b):
    """Multiply two numbers"""
    return a * b  # This seems odd

def divide(a, b):
    if b == 0:
        return "error"
    """Divide a by b"""
    return a / b  # What if b is 0?

def calculate(expression):
    """Parse and calculate an expression like '5 + 3'"""
    parts = expression.split()
    
    if len(parts) != 3:
        print("Invalid expression format")
        return None
    try:
        a = float(parts[0])  # Should this be converted?
        operator = parts[1]
        b = float(parts[2])  # Should this be converted?
    except (ValueError,ZeroDivisionError):
        return "error"
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        pass  # Silent failure?

def interactive_mode():
    """Interactive calculator mode"""
    print("=" * 40)
    print("BLACK BOX CALCULATOR")
    print("=" * 40)
    print("Enter calculations like: 5 + 3")
    print("Type 'quit' to exit")
    print("=" * 40)
    
    while True:
        print()
        user_input = input("> ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
        
        result = calculate(user_input)
        
        if result is not None:
            print(f"Result: {result}")
        else:
            print(f"ERROR!!!")

def test_mode():
    """Run predefined tests"""
    print("Running tests...")
    print("-" * 40)
    
    test_cases = [
        ("5 + 3", 8),
        ("10 - 2", 8),
        ("4 * 5", 20),
        ("15 / 3", 5.0),
        ("5 / 0", "error"),  # Should handle gracefully
        ("abc + 3", "error"),  # Invalid input
    ]
    
    for expression, expected in test_cases:
        print(f"\nTest: {expression}")
        print(f"Expected: {expected}")
        
        try:
            result = calculate(expression)
            print(f"Got: {result}")
            
            if result == expected:
                print("✓ PASS")
            else:
                print("✗ FAIL - Unexpected result")
        except Exception as e:
            print(f"✗ ERROR: {type(e).__name__}: {e}")
    
    print("-" * 40)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_mode()
    else:
        interactive_mode()
