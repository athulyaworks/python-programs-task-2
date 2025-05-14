#Calculate the power of a number without using **. 

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1

for _ in range(exponent):
    result *= base
print(f"{base} raised to the power of {exponent} is: {result}")