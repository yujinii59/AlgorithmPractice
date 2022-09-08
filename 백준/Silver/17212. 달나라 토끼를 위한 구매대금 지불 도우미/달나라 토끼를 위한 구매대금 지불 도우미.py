def payment_way(num, ways):
    way = ways[i-1]+1
    if i >= 2:
        way = min(way, ways[i-2]+1)
    if i >= 5:
        way = min(way, ways[i-5]+1)
    if i >= 7:
        way = min(way, ways[i-7]+1)
        
    return way

n = int(input())
ways = [0]*(n+1)
for i in range(1,n+1):
    ways[i] = payment_way(i, ways)

print(ways[n])