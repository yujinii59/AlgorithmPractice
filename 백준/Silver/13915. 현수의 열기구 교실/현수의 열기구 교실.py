while True:
    try:
        n = int(input())
        scores = {}
        for _ in range(n):
            score = ''.join(sorted(list(set(input()))))
            scores[score] = 1
            
        print(len(scores))
    except:
        break