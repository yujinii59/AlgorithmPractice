def solution(A, B):
    answer = 0
    A = sorted(A, reverse=True)
    B = sorted(B)
    max_num = B.pop()
    for num in A:
        if num < max_num:
            if B:
                max_num = B.pop()
            answer += 1
    return answer