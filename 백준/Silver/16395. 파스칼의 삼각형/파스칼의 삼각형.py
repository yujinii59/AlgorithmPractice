from math import factorial
n, k = map(int, input().split())
print(factorial(n-1) // (factorial(n-k) * factorial(k-1)))