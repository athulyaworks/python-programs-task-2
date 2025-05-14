#Replace negative numbers in a list with zero. 

nums = list(map(int, input("Enter numbers separated by space: ").split()))

for i in range(len(nums)):
    if nums[i] < 0:
        nums[i] = 0

print("Updated list:", nums)
