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
                print("Cannot divided by zero!")
                return
            result = num1 / num2
        case _:
            print("Invalid Operator!")
            return

    print(f"Result: {result}")


while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    calculator(num1, num2, operator)

    choice = input("Do you want to continue? (y/n): ").lower()

    if choice != "y":
        print("Goodbye!")
        break
