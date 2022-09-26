n = int(input())
counts = [0]*500001
seq = list(map(int, input().split()))
whole = sum(seq)
total = 0
for num in seq:
    whole -= num
    total += num * whole
    
print(total%1000000007)