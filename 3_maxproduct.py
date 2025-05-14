#Find the maximum product of two integers in a list. 

user_input = input("Enter a list of integers separated by space: ")

numbers = user_input.split()
numbers = [int(num) for num in numbers]

max_product = numbers[0] * numbers[1]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        product = numbers[i] * numbers[j]
        if product > max_product:
            max_product = product

print("Maximum product of two integers in the list:", max_product)