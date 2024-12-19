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

def modulus(num1, num2):
    return num1 % num2

def exponent(num1, num2):
    return num1**num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulus,
    "**": exponent,
}


# Main Execution:
# Input Gathering
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

calculation_in_progress = True
result = 0

while calculation_in_progress:

    for operator_symbol in operations:
        print(operator_symbol)

    operation = input("Choose an operation Please : ")
    # Operator Validation
    while operation not in ["+", "-", "*", "/", "%", "**"]:
        print("Invalid operation!")
        operation = input("Please choose a valid operation symbol :  ")

    result = operations[operation](num1, num2)  # VIP

    print(f"Your result is: {num1} {operation} {num2} = {result}")
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
            print("Starting a new calculation")
            print("\n" * 20)
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
    elif repetition == "exit":
        print("Goodbye!")
        calculation_in_progress = False
