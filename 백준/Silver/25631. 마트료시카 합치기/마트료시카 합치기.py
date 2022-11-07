n = int(input())
sizes = sorted(list(map(int, input().split())))
Матрёшка = [int(1e9)+1]
while sizes:
    size = sizes.pop()
    for i in range(len(Матрёшка)):
        if Матрёшка[i] > size:
            Матрёшка[i] = size
            break
    else:
        Матрёшка.append(size)
    
print(len(Матрёшка))