#Count how many elements in a list are greater than the average. 

nums = list(map(int, input("Enter numbers separated by space: ").split()))
avg = sum(nums) / len(nums)

count = 0
for num in nums:
    if num > avg:
        count += 1
print("Average is:", avg)
print("Count of numbers greater than average:", count)
