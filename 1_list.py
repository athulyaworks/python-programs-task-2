#Find the common elements in two lists.

list1 = input("Enter first list separated by space: ").split()
list2 = input("Enter second list separated by space: ").split()

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)

