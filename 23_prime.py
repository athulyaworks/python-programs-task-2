#Use filter() to get only prime numbers from a list. 

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

nums = list(map(int, input("Enter numbers by adding space: ").split()))

primes = list(filter(is_prime, nums))

print("Prime numbers:", primes)
