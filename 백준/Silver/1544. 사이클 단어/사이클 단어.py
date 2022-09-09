n = int(input())
words = []
for _ in range(n):
    word = input()
    add = True
    for w in words:
        if word in w and len(word) == len(w) // 2:
            add = False
            break
    if add:
        words.append(word*2)
        
print(len(words))