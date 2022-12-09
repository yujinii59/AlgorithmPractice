t = int(input())
for _ in range(t):
    sounds = input().split()
    others = set()
    while True:
        string = input()
        if string == 'what does the fox say?':
            break
        others.add(string.split()[-1])
    for sound in sounds:
        if sound not in others:
            print(sound, end=' ')
    print()