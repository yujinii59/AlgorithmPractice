from collections import deque

def solution(order):
    queue = deque(list(range(1, len(order)+1)))
    stack = []
    cnt = 0
    main = queue.popleft()
    sub = 0
    for num in order:
        while num > main:
            if sub:
                stack.append(sub)
            sub = main
            main = queue.popleft()
        if num == main:
            if queue:
                main = queue.popleft()
            else:
                main += 1
            cnt += 1
        elif num == sub:
            if stack:
                sub = stack.pop()
            else:
                sub = 0
            cnt += 1
        else:
            break
    return cnt