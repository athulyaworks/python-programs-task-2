#Write a recursive function to calculate the nth Fibonacci number. 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter a number: "))
print("Fibonacci number is:", fibonacci(n))

