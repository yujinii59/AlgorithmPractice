n = int(input())
alphabets = {}
words = []
for _ in range(n):
    word = input()
    words.append(word)
    length = len(word)
    for i in range(length):
        if alphabets.get(word[i], 0):
            alphabets[word[i]] += 10 ** (length-i-1)
        else:
            alphabets[word[i]] = 10 ** (length-i-1)

alphabets = sorted(alphabets.items(), key=lambda x: -x[1])

total = 0
for i, (_,val) in enumerate(alphabets):
    total += val * (9-i)
    
print(total)
