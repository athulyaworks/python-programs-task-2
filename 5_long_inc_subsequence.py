# Find the longest increasing subsequence in a list

nums = list(map(int, input("Enter numbers separated by space: ").split()))

subsequences = [[] for _ in range(len(nums))]

for i in range(len(nums)):
    subsequences[i] = [nums[i]]
    for j in range(i):
        if nums[j] < nums[i] and len(subsequences[j]) + 1 > len(subsequences[i]):
            subsequences[i] = subsequences[j] + [nums[i]]

longest = max(subsequences, key=len)
print("Longest Increasing Subsequence:", longest)
