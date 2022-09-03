import sys
n = int(sys.stdin.readline())
cards = {}
for _ in range(n):
    num = int(sys.stdin.readline())
    if cards.get(num, 0):
        cards[num] += 1
    else:
        cards[num] = 1
        
cards = sorted(cards.items(), key=lambda x: [-x[1], x[0]])
print(cards[0][0])