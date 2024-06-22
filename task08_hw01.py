x = eval(input())

def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

f = 0
for j in range(1, x+1):
    f += factorial(j)

print(f)
