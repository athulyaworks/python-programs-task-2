#Write a recursive function to calculate GCD. 

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD is:", gcd(num1, num2))
