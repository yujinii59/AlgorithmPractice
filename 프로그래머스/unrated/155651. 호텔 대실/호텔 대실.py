import heapq
import datetime

def solution(book_time):
    check_out = []
    book_time = sorted(book_time)
    answer = 0
    for s, e in book_time:
        s = datetime.datetime.strptime(s, '%H:%M')
        while check_out and s >= heapq.nsmallest(1, check_out)[0]:
            heapq.heappop(check_out)
        heapq.heappush(check_out, datetime.datetime.strptime(e, '%H:%M') + datetime.timedelta(minutes=10))
        answer = max(len(check_out), answer)
    return answer