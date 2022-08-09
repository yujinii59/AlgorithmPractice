from copy import deepcopy

n = int(input())
friends = [[0] * n for _ in range(n)]
for i in range(n):
    conn = input()
    for j in range(n):
        if conn[j] == 'Y':
            friends[i][j] = 1
            
friends_tmp = deepcopy(friends)
for k in range(n):
    for i in range(n):
        if friends[i][k] == 1:
            for j in range(i+1, n):
                if friends[k][j] == 1:
                    friends_tmp[i][j] = 1
                    friends_tmp[j][i] = 1
                    
max_cnt = 0
for i in range(n):
    max_cnt = max(max_cnt, sum(friends_tmp[i]))
    
print(max_cnt)
