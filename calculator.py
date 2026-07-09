def calculator(num1, num2, operator):
    match operator:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                print("Cannot divide by zero!")
                return
            result = num1 / num2

    print(f"Result: {result:.2f}")


while True:

    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Please enter a valid first number!")

    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Please enter a valid second number!")

    while True:
        operator = input("Enter operator (+, -, *, /): ")

        if operator in ["+", "-", "*", "/"]:
            break

        print("Invalid operator! Please try again.")

    calculator(num1, num2, operator)

    while True:
        choice = input("Do you want to continue? (y/n): ").strip().lower()

        if choice in ["y", "n"]:
            break

        print("Please enter 'y' or 'n'.")

    if choice == "n":
        print("Goodbye!")
        break
