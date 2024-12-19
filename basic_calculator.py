import art

print("Welcome to the Calculator")
print(art.logo)

# Function Definitions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# Main Execution
# Input Gathering
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

calculation_in_progress = True
result = 0

while calculation_in_progress:
    # Operator Validation
    operation = input(
        "Choose an operation: + for addition, - for subtraction, * for multiplication, / for division: "
    )
    while operation not in ["+", "-", "*", "/"]:
        print("Invalid operation!")
        operation = input("Please enter a valid operation: (+, -, *, /) ")

    # Perform the selected operation
    if operation == "+":
        result = add(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    else:
        print("Invalid operation")
        break

    print(f"The result is: {result}")
    repetition = (
        input(
            'Do you want to continue using last result or start new calculation? "yes" continue or "no" to start new Operations or "exit" to exit: '
        )
        .strip()
        .lower()
    )
    if repetition in ["yes", "no"]:
        if repetition == "yes":
            num1 = result
            num2 = int(input("Enter the second number: "))
        else:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
    elif repetition == "exit":
        print("Goodbye!")
        calculation_in_progress = False
