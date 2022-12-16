t = int(input())
for _ in range(t):
    n = int(input())
    ls = [0]+[int(input()) for _ in range(n)]
    
    visited = [0]*(n+1)
    curr = [1]
    cnt = 0
    while curr:
        num = curr.pop()
        if num != n:
            if visited[num]:
                print(0)
                break
            else:
                cnt += 1
                visited[num] = 1
                curr.append(ls[num])
    else:
        print(cnt)
        