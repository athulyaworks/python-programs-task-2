#Write a function to find the median of a list. 

def find_median(numbers):
    numbers.sort()  
    n = len(numbers)
    
    if n % 2 == 1:       
        return numbers[n // 2]
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return (mid1 + mid2) / 2

nums = list(map(int, input("Enter numbers separated by space: ").split()))
median = find_median(nums)
print("Median is:", median)
