a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose operation: +, -, *, /")
op = input("Enter your choice: ")

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    if b != 0:
        result = a / b
    else:
        print("Division by zero not possible")
        exit()
else:
    print("Invalid operation!")
    exit()

print("Result =", result)
