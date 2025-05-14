#Sort a list of tuples by the second element. 

n = int(input("How many items? "))

items = []

for i in range(n):
    a, b = input("Enter two values like name number: ").split()
    items.append((a, int(b)))


def sort_by_second(item):
    return item[1]

items.sort(key=sort_by_second)

print("Sorted list by second value:", items)
