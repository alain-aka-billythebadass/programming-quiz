# Name: Alain
# Addition/Subtraction Program

# Functions for extra credit
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

operation = "addition"  
num1 = 7
num2 = 3

print("Operation:", operation)
print("Numbers:", num1, num2)

if operation == "addition":
    result = add(num1, num2)
    print("Result:", result)
elif operation == "subtraction":
    result = subtract(num1, num2)
    print("Result:", result)
else:
    print("Invalid operation")
