from math import factorial

def solution(n, k):
    answer = []
    nums = list(range(1, n+1))
    case_cnt = factorial(n-1)
    k -= 1
    for i in range(n-1, 0, -1):
        q, k = divmod(k, case_cnt)
        case_cnt //= i
        answer.append(nums.pop(q))
    answer.append(nums.pop())
    return answer