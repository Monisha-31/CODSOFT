def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    number1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    number2 = float(input("Enter second number: "))

    if op == '+':
        result = number1 + number2
    elif op == '-':
        result = number1 - number2
    elif op == '*':
        result = number1 * number2
    elif op == '/':
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operator!"

    print("Result:", result)


calculator()