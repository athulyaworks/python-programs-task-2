#Count the number of trailing zeroes in a factorial. 

n = int(input("Enter a number: "))

count = 0
i = 5

while n // i > 0:
    count += n // i
    i *= 5

print("Number of trailing zeros in", n, "factorial is:", count)
