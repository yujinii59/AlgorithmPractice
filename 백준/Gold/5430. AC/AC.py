import sys

t = int(input())
for _ in range(t):
    operations = sys.stdin.readline().rstrip()
    d_cnt = operations.count('D')
    n = int(sys.stdin.readline())
    ls = sys.stdin.readline().rstrip()
    if d_cnt > n:
        print('error')
    else:
        if n != 0:
            ls = list(map(int, ls.replace('[','').replace(']', '').split(',')))
            rng = [0, -n]
            target = 0
            for op in operations:
                if op == 'R':
                    target = (target + 1) % 2
                else:
                    rng[target] += 1
            if target == 0:            
                print('['+','.join(map(str, ls[rng[0] : -rng[1]]))+']')
            else:
                print('['+','.join(map(str, list(reversed(ls[rng[0] : -rng[1]]))))+']')
        else:
            ls = []
            print(ls)