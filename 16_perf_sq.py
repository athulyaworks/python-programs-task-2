#Check whether a number is a perfect square. 

num = int(input("Enter a number: "))

i = 1
found = False

while i * i <= num:
    if i * i == num:
        found = True
        break
    i += 1

if found:
    print(num, "is a perfect square.")
else:
    print(num, "is not a perfect square.")
    