t = int(input())
for _ in range(t):
    n = int(input())
    total = 0
    max_voted = [0, 0]
    for i in range(n):
        voted = int(input())
        total += voted
        if max_voted[0] < voted:
            max_voted = [voted, i+1]
        elif max_voted[0] == voted:
            max_voted[1] = 0
            
    if max_voted[1] == 0:
        print('no winner')
    else:
        if max_voted[0] > total / 2:
            print(f'majority winner {max_voted[1]}')
        else:
            print(f'minority winner {max_voted[1]}')