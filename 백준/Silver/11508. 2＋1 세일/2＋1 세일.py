import sys
input = sys.stdin.readline

n = int(input())
prices = sorted([int(input()) for _ in range(n)], reverse=True)
total = 0
for i in range(0, n, 3):
    total += sum(prices[i:i+2])
    
print(total)