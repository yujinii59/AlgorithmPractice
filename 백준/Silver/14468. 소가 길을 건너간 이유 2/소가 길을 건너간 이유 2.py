string = input()
l = len(string)
cows = {}
for i in range(l):
    if not cows.get(string[i], 0):
        roads = []
        for j in range(i+1, l):
            if string[j] != string[i]:
                if string[j] in roads:
                    roads.remove(string[j])
                else:
                    roads.append(string[j])
            else:
                cows[string[i]] = len(roads) + 1
                break
print((sum(cows.values())-(l//2)) // 2)