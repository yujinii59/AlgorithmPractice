cards = {'P':list(range(1, 14)), 'K':list(range(1, 14)), 'H':list(range(1, 14)), 'T':list(range(1, 14))}
s = input()
b = True
for i in range(0, len(s), 3):
    shape = s[i]
    num = int(s[i+1:i+3])
    if num in cards[shape]:
        cards[shape].remove(num)
    else:
        b = False
        break
if b:
    for ls in cards.values():
        print(len(ls), end=' ')
else:
    print('GRESKA')