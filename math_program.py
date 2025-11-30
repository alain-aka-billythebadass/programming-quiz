# Name:Alain
# Who I collaborated with:Noone

# EXTRA CREDIT

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b


print("Welcome to the Math Program!")
operation = input("Do you want to do addition or subtraction? ").strip().lower()


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if operation == "addition":
    result = add_numbers(num1, num2)
    print("The result is:", result)

elif operation == "subtraction":
    result = subtract_numbers(num1, num2)
    print("The result is:", result)

else:
    print("Invalid choice. Please type 'addition' or 'subtraction'.")
