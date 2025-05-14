# Flatten a nested list.

flat_list = []

n = int(input("Enter how many sublists?: "))

for i in range(n):
    numbers = list(map(int, input("Enter sublist separated by space: ").split()))
    flat_list.extend(numbers)

# unique_list = []
# for item in flat_list:
#     if item not in unique_list:
#         unique_list.append(item)

print("Flattened list:", flat_list)
# print("Flattened list with unique elements:", unique_list)
