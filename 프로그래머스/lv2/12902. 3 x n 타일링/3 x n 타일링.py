def solution(n):
    if n % 2:
        return 0
    
    case = [1]
    for i in range(n//2):
        total = sum(case[:-1])
        case.append(case[i]*3 + 2*total)
    answer = case[n//2] % 1000000007
    return answer