#Implement a simple closure example that remembers state. 

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

my_counter = make_counter()

# Calling the counter 
print(my_counter())  
print(my_counter())  
print(my_counter())  
