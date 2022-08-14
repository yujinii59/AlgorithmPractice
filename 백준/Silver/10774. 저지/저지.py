n = int(input())
k = int(input())
sizes = {'S': 1, 'M': 2, 'L': 3}
judge = {}
for j in range(n):
    size = input()
    judge[str(j+1)] = size
      
cnt = 0
for _ in range(k):
    size, num = input().split()
    if not judge.get(num, 0):
        continue
    judge_size = judge[num]
    if sizes[judge_size] >= sizes[size]:
        cnt += 1
        del judge[num]
        
print(cnt)