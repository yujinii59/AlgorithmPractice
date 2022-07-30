def action(kind, state, score):
    if kind == 'a':    
        if state[1] & state[2] & state[3]:
            score += 1
            state[3] = 0
        if state[1] & state[2]:
            state[3] = 1
            state[2] = 0
        if state[1]:
            state[2] = 1
            state[1] = 0
        state[1] = 1
    else:
        if state[3]:
            score += 1
            state[3] = 0
        if state[2]:
            state[3] = 1
            state[2] = 0
        if state[1]:
            state[2] = 1
            state[1] = 0
            
    return state, score

n = int(input())
state = {0: 0, 1: 0, 2: 0, 3: 0}
kinds = list(map(int, input().split()))

ball = 0
score = 0
for kind in kinds:
    if kind == 1:
        ball += 1
        if ball == 4:
            state, score = action(kind='a', state=state, score=score)
            ball = 0
    elif kind == 2:
        state, score = action(kind='a', state=state, score=score)
        ball = 0
    elif kind == 3:
        state, score = action(kind='b', state=state, score=score)
        ball += 1
        if ball == 4:
            state, score = action(kind='a', state=state, score=score)
            ball = 0

print(score)