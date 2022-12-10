n, w = map(int, input().split())
coin = 0
prev = int(input())
for _ in range(n-1):
    curr = int(input())
    if prev < curr:
        coin += w // prev
        w %= prev
    elif prev > curr:
        w += coin*prev
        coin = 0
    
    prev = curr

if coin:
    w += coin * prev
    
print(w)