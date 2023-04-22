import heapq

def solution(k, score):
    q = []
    answer = []
    for num in score:
        if len(q) < k:
            heapq.heappush(q, num)
            min_score = heapq.nsmallest(1,q)[0]
            
        else:
            min_score = heapq.heappop(q)
            if min_score < num:
                heapq.heappush(q, num)
                min_score = heapq.nsmallest(1,q)[0]
            else:
                heapq.heappush(q, min_score)
        answer.append(min_score)
    return answer