#Build a menu-driven program using functions e.g., calculator. 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def modulus(x, y):
    return x % y

def exponent(x, y):
    return x ** y

def menu():
    print("\nSimple Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponent")
    print("7. Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    while True:
        menu()
        choice = input("Select operation (1-7): ")

        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {modulus(num1, num2)}")
            elif choice == '6':
                print(f"Result: {exponent(num1, num2)}")
        else:
            print("Invalid input! Please select a valid operation.")
            
calculator()
