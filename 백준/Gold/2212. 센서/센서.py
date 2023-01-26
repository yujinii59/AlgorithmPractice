n = int(input())
k = int(input())
sensors = sorted(list(set(map(int, input().split()))))
n = len(sensors)

lengths = []
for i in range(n-1):
    lengths.append(sensors[i+1]-sensors[i])
    
print(sum(sorted(lengths, reverse=True)[k-1:]))