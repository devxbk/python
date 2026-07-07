def calculator(num1, num2, operator):
    match operator:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            result = num1 / num2
        case _:
            print("Invalid Operator!")
            return

    print(f"Result: {result}")


calculator(num1, num2, operator)

while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")
