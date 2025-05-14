#Split a list into chunks of size n. 

items = input("Enter list items in space-separated: ").split()
n = int(input("Enter chunk size: "))

chunks = []
for i in range(0, len(items), n):
    chunks.append(items[i:i+n])
print("Chunks:", chunks)
