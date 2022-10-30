import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(n, robot):
    for i in range(n):
        if len(robot) == 1:
            break

        temp = {}
        for num, val in robot.items():
            if val[i] in temp:
                temp[val[i]].append(num)
            else:
                temp[val[i]] = [num]
        lose = get_loser(temp)
        if lose != 'X':
            losers = temp[lose]
            for loser in losers:
                robot.pop(loser)

    if len(robot) == 1:
        result = list(robot.keys())[0]
    else:
        result = 0

    return result

def get_loser(temp):
    lose = 'X'
    if len(temp) == 2:
        if 'R' not in temp:
            lose = 'P'
        elif 'S' not in temp:
            lose = 'R'
        else:
            lose = 'S'

    return lose

t = int(input())
for _ in range(t):
    n = int(input())
    robot = {(i + 1): input() for i in range(n)}
    result = solution(len(robot[1]), robot)
    print(result)
