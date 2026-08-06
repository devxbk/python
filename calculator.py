"""
Simple Calculator
Performs addition, subtraction, multiplication, and division.
"""


def calculator(num1, num2, operator):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                return None
            return num1 / num2
        case _:
            return "Invalid"


print("=" * 35)
print("      SIMPLE CALCULATOR")
print("=" * 35)

while True:

    # Get first number
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    # Get second number
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    # Get operator
    while True:
        operator = input("Enter operator (+, -, *, /): ")

        if operator in ("+", "-", "*", "/"):
            break

        print("Invalid operator! Please try again.")

    # Perform calculation
    result = calculator(num1, num2, operator)

    # Display result
    if result is None:
        print("Cannot divide by zero!")
    elif result == "Invalid":
        print("Invalid operation!")
    else:
        print(f"Result: {result:.2f}")

    # Continue or exit
    while True:
        choice = input("Do you want to continue? (y/n): ").lower()

        if choice in ("y", "n"):
            break

        print("Please enter 'y' or 'n'.")

    if choice == "n":
        print("Thank you for using the calculator!")
        break
