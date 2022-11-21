from heapq import heappush, heappop
n = int(input())
neg = []
pos = []
zero = 0
for _ in range(n):
    num = int(input())
    if num < 0:
        heappush(neg, num)
    elif num == 0:
        zero += 1
    else:
        heappush(pos, -num)
        
total = 0
while len(neg) >= 2:
    total += heappop(neg)*heappop(neg)
    
if neg and zero==0:
    total += heappop(neg)
    
while len(pos) >= 2:
    num1, num2 = heappop(pos), heappop(pos)
    if num1 == -1 or num2 == -1:
        total -= num1 + num2
    else:
        total += num1 * num2 
    
if pos:
    total -= heappop(pos)
    
print(total)