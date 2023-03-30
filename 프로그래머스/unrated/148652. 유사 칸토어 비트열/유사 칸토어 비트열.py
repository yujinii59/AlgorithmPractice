def solution(n, l, r):
    answer = 0
    if n == 1:
        for i in range(l, r + 1):
            if i != 3:
                answer += 1
    else:
        if (l-1) // (5 ** (n - 1)) == (r-1) // (5 ** (n - 1)):
            lres = (l - 1) % (5 ** (n - 1))
            rres = r % (5 ** (n - 1))
            if lres:
                if (l - 1) // (5 ** (n - 1)) + 1 != 3:
                    if rres:
                        answer += solution(n - 1, lres + 1, rres)
                    else:
                        answer += solution(n-1, lres+1, 5**(n-1))
            else:
                if r // (5 ** (n - 1)) != 2:
                    answer += solution(n - 1, 1, rres)
        else:
            res = (l - 1) % (5 ** (n - 1))
            if res:
                left = (l - 1) // (5 ** (n - 1)) + 1
                if left != 3:
                    answer += solution(n - 1, res + 1, 5 ** (n - 1))
            else:
                left = l // (5 ** (n - 1))

            res = r % (5 ** (n - 1))
            if res:
                right = r // (5 ** (n - 1))
                if right != 2:
                    answer += solution(n - 1, 1, res)
            else:
                right = r // (5 ** (n - 1))
            print(left, right, answer)
            for i in range(left, right):
                if i != 2:
                    answer += 4 ** (n-1)
    return answer