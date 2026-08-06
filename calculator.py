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
            return None


print("=" * 35)
print("      SIMPLE CALCULATOR")
print("=" * 35)

while True:

    # First number
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    # Second number
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Please enter a valid number!")

    # Operator
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
    else:
        print(f"Result: {result:.2f}")

    # Continue?
    while True:
        choice = input("Do you want to continue? (y/n): ").lower()

        if choice in ("y", "n"):
            break

        print("Please enter 'y' or 'n'.")

    if choice == "n":
        print("Thank you for using the calculator. Goodbye!")
        break
