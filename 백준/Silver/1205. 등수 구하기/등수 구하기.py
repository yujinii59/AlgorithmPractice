n, score, p = map(int, input().split())
if n > 0:
    rank = sorted(list(map(int, input().split())), reverse=True)
    if n == p:
        if score <= rank[-1]:
            print(-1)
        else:
            for i in range(n):
                if score > rank[i]:
                    rnk = i + 1
                    break
                elif score == rank[i]:
                    rnk = i + 1
                    break
            print(rnk)
    else:
        rnk = n + 1
        for i in range(n):
            if score > rank[i]:
                rnk = i + 1
                break
            elif score == rank[i]:
                rnk = i + 1
                break
        print(rnk)
else:
    print(1)