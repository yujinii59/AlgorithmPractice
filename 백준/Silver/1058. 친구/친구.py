n = int(input())
friends = []
counts = []
for i in range(n):
    friend = input()
    friends.append([])
    for j, f in enumerate(friend):
        if f == 'Y':
            friends[i].append(j)
            
for i in range(n):
    conn = friends[i][:]
    counts.append(friends[i][:])
    for c in conn:
        add = friends[c][:]
        add.remove(i)
        counts[i].extend(add)

    counts[i] = len(set(counts[i]))

max_cnt = 0
for cnt in counts:
    max_cnt = max(max_cnt, cnt)
print(max_cnt)