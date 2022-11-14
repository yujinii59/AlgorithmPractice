n, l = map(int, input().split())
heights = sorted(list(map(int, input().split())))

for height in heights:
    if height > l:
        break
    else:
        l += 1
        
print(l)