n = int(input())
cases = {}
person = set()
for _ in range(n):
    name, place, s, e = input().split()
    if name in person:
        continue
    person.add(name)
    for i in range(int(s), int(e)):
        cnt = cases.get((place, i), 0)
        cases[(place, i)] = cnt + 1

cases = sorted(cases.items(), key=lambda x: [-x[1], x[0][0], x[0][1]])
cnt = cases[0][1]
places = []
place = cases[0][0][0]
time = -15
for case, count in cases:
    if place == case[0]:
        if time + 1 == case[1]:
            places[-1][1] += 1
        else:
            places.append([case[1], 1])

    else:
        break
    time = case[1]

print(place, places[0][0], places[0][0] + places[0][1])