def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    except ValueError:
        print("Enter a number!")
        return

    operator = input("Select an operator ( +, -, *, /): ")

    if operator == "+":
        print(f"The result is: {num1+num2}")
    elif operator == "-":
        print(f"The result is: {num1-num2}")
    elif operator == "*":
        print(f"The result is: {num1*num2}")
    elif operator == "/":
        if num2 == 0:
            print("Can't divided by Zero!")
        else:
            print(f"The result is: {num1/num2}")
    else:
        print("Invalid operator!")


calculator()
