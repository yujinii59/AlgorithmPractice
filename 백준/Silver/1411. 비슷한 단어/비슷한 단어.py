n = int(input())
words = {}
for _ in range(n):
    string = input()
    alpha = {}
    word = ''
    i = 1
    for s in string:
        if alpha.get(s, 0):
            word += alpha[s]
        else:
            alpha[s] = str(i)
            word += alpha[s]
            i += 1
    if words.get(word, 0):
        words[word] += 1
    else:
        words[word] = 1

pair = 0        
for cnt in words.values():
    pair += cnt * (cnt-1) // 2
    
print(pair)