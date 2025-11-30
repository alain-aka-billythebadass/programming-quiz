# Name: Alain
# Collaborators: None

# Simple functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

operation = "addition"  # change to "subtraction" if you want
num1 = 7
num2 = 3

print("Operation:", operation)
print("Numbers:", num1, num2)

if operation == "addition":
    print("Result:", add(num1, num2))
elif operation == "subtraction":
    print("Result:", subtract(num1, num2))
