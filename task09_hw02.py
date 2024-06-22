x = eval(input())

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
        
    return True

def primes(n):
    for j in range(2, n+1):
        if isPrime(j) is True:
            print(j, end = ' ')

primes(x)
