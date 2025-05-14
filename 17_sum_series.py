#Find the sum of the series: 1² + 2² + 3² + ... + n². 

n = int(input("Enter a number: "))
sum_of_squares = 0

for i in range(1, n + 1):
    sum_of_squares += i * i

print("The sum of the series 1² + 2² + ... +", n, "² is:", sum_of_squares)
