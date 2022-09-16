r, c = map(int, input().split())
puzzle = []
words = []
for _ in range(r):
    row = input()
    cnt = 0
    ss = ''
    for s in row:
        if s == '#':
            if cnt > 1:
                words.append(ss)
            ss = ''
            cnt = 0
        else:
            ss += s
            cnt += 1
            
    if cnt > 1:
        words.append(ss)
    puzzle.append(row)
    
for i in range(c):
    cnt = 0
    ss = ''
    for j in range(r):
        if puzzle[j][i] == '#': 
            if cnt > 1:
                words.append(ss)
            ss = ''
            cnt = 0
        else:
            ss += puzzle[j][i]
            cnt += 1
            
    if cnt > 1:
        words.append(ss)

print(sorted(words)[0])