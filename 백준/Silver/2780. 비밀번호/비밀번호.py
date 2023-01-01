t = int(input())
keypad = [[1,2,3],[4,5,6], [7,8,9],[0]]
moves = [(-1,0), (0,-1), (0,1), (1, 0)]
conn = {i:[] for i in range(10)}
for i in range(4):
    if i == 3:
        l = 1
    else:
        l = 3
    for j in range(l):
        num = keypad[i][j]
        for move in moves:
            r = i+move[0]
            c = j+move[1]
            if r == 3 and  c >= 1:
                    continue
            elif r < 0 or r >= 4 or c < 0 or c >= l:
                continue
            conn[num].append(keypad[r][c])
        

for _ in range(t):
    n = int(input())
    cases = [[0]*10 for _ in range(n)]
    cases[0] = [1]*10
    for i in range(1, n):
        for j in range(10):
            for num in conn[j]:
                cases[i][j] += cases[i-1][num]
    print(sum(cases[n-1])%1234567)