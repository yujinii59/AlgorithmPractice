n = int(input())
cards = [int(input()) for _ in range(n)]
cnt = 0
next = cards.index(1)
card = 2
while card <= n:
    prev = next
    next = cards.index(card)
    if prev > next:
        cnt += 1
    else:
        card += 1
print(cnt)