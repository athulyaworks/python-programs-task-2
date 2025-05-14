#Create a function that accepts any number of positional and keyword arguments. 

def my_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

positional = input("Enter some values (space-separated): ").split()


args = []
for item in positional:
    if item.isdigit():
        args.append(int(item))
    else:
        args.append(item)

kwargs = {}
count = int(input("How many keyword arguments? "))
for _ in range(count):
    key = input("Enter key: ")
    value = input("Enter value: ")
    kwargs[key] = value

my_function(*args, **kwargs)

