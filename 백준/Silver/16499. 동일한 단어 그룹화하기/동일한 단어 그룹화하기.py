n = int(input())
words = set()
for _ in range(n):
    words.add(''.join(sorted(input())))
    
print(len(words))