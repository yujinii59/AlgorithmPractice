k, l = map(int, input().split())
sugang = {}
for i in range(l):
    sugang[input()] = i
    
sugang = sorted(sugang.items(), key=lambda x: x[1])
for num, idx in sugang[:k]:
    print(num)