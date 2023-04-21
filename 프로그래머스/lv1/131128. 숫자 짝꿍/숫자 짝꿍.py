from collections import Counter

def solution(X, Y):
    answer = ''
    Xcounter = Counter(X)
    Ycounter = Counter(Y)
    Xset = set(X)
    Yset = set(Y)
    common = sorted(list(Xset & Yset), reverse=True)
    if len(common) == 0:
        return "-1"
    
    if common == ["0"]:
        return "0"
    
    for num in common:
        answer += num * min(Xcounter[num], Ycounter[num])
    
    return answer