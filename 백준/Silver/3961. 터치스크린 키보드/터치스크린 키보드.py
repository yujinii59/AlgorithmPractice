alphabets = ['qwertyuiop','asdfghjkl','zxcvbnm']
loc_of_alphabet = {}
for i, alphabet in enumerate(alphabets):
    for j, a in enumerate(alphabet):
        loc_of_alphabet[a] = (i, j)

t = int(input())
for _ in range(t):
    word, n = input().split()
    l = len(word)
    loc_of_word = [loc_of_alphabet[w] for w in word]
    dist = {}
    for _ in range(int(n)):
        cnt = 0
        rec = input()
        for i in range(l):
            r, c = loc_of_alphabet[rec[i]]
            row, col = loc_of_word[i]
            cnt += abs(row-r) + abs(col-c)
        dist[rec] = cnt
    dist = sorted(dist.items(), key=lambda x:[x[1], x[0]])
    for w, d in dist:
        print(w, d)