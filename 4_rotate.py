#Rotate a list by k elements. 

user_input = input("Enter a list of integers separated by space: ")
lst = [int(x) for x in user_input.split()]

k = int(input("Enter the number of elements to rotate: "))
k = k % len(lst)                                           #rotate the list
rotated_list = lst[k:] + lst[:k]

print("Rotated list:", rotated_list)