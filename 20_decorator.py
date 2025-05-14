#Create a decorator that logs the execution time of a function. 

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time taken:", end - start, "seconds")
    return wrapper

@timer
def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

greet_user()



