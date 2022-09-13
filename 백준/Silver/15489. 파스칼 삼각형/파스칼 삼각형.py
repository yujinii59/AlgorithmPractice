from math import factorial

r, c, w = map(int, input().split())
r -= 1
c -= 1
total = 0
for i in range(w):
    for j in range(i+1):
        total += factorial(r+i) // (factorial(r+i-(c+j)) * factorial(c+j))

print(total)