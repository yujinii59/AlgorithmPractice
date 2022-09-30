t = int(input())
for _ in range(t):
    infos = list(map(int, input().split()))
    n = infos[0]
    perc = infos[1:3]
    goal = infos[3:]
    pass_p = {}
    dribble = {}
    pass_p[1] = list(map(int, input().split()))
    dribble[1] = list(map(int, input().split()))
    pass_p[2] = list(map(int, input().split()))
    dribble[2] = list(map(int, input().split()))
    for i in range(n-1):
        tmp = [
            min(perc[0]+dribble[1][i], perc[1]+pass_p[2][i]),
            min(perc[1]+dribble[2][i], perc[0]+pass_p[1][i])
        ]
        perc = tmp
    print(min(perc[0]+goal[0], perc[1]+goal[1]))