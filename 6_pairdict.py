#Pair elements from two lists into a dictionary. 

keys = input("Enter keys: ").split()
values = input("Enter values: ").split()

result = dict(zip(keys, values))

print(result)
