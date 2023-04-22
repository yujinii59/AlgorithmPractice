from math import ceil

def solution(n, stations, w):
    answer = 0
    end = 0
    for station in stations:
        if end < station - (w+1):
            answer += ceil((station - (w+1) - end) / (2*w+1))
        end = station + w
        
    if end < n:
        answer += ceil((n-end) / (2*w+1))
    return answer