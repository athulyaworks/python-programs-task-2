#Use lambda to sort a list of dictionaries by a key. 

people = []

n = int(input("How many people? "))

for i in range(n):
    name, age = input("Enter name and age: ").split()
    people.append({"name": name, "age": int(age)})

people.sort(key=lambda x: x["age"])

print("Sorted by age:")
for person in people:
    print(person)
