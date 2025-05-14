# Create a calculator using if and elif.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Select operation: + , -, *, /")
op = input("Enter operation: ")


if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("Cannot divide by zero")
        result = None
    else:
        result = num1 / num2
else:
    print("Invalid operation")
    result = None


if result is not None:
    print("Result:", result)
