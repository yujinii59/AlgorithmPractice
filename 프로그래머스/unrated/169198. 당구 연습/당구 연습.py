from math import sqrt

def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        cases = []
        if x == startX:
            if y >= startY:
                cases.append((y+startY)**2)
            if y <= startY:
                cases.append((2*n - y - startY)**2)
        else:
            cases.append((x-startX)**2 + (y+startY)**2)
            cases.append((x-startX)**2 + (2*n - y - startY)**2)
                
        
        if y == startY:
            if x >= startX:
                cases.append((x+startX)**2)
            if x <= startX:
                cases.append((2*m - x - startX)**2)
        else:
            cases.append((y-startY)**2 + (x+startX)**2)
            cases.append((y-startY)**2 + (2*m - x - startX)**2)
        
        answer.append(min(cases))
    return answer