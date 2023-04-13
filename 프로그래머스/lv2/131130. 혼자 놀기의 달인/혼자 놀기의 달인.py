def solution(cards):
    length = len(cards)
    visited = [0 for _ in range(length + 1)]
    cards = [0] + cards
    cnts = []
    for i in range(length):
        idx = i + 1
        cnt = 0
        while visited[idx] == 0:
            cnt += 1
            visited[idx] = 1
            idx = cards[idx]
        if cnt:
            cnts.append(cnt)

    if len(cnts) < 2:
        return 0
    else:
        cnts = sorted(cnts, reverse=True)
        return cnts[0] * cnts[1]