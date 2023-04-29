import heapq

def solution(operations):
    answer = []
    num_set = set()
    max_heap = []
    min_heap = []
    for operator in operations:
        op, num = operator.split()
        num = int(num)
        if op == 'I':
            num_set.add(num)
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        else:
            pop_num = int(1e10)
            while num_set and pop_num not in num_set:
                if num == 1:
                    pop_num = -heapq.heappop(max_heap)
                else:
                    pop_num = heapq.heappop(min_heap)
            if num_set:
                num_set.discard(pop_num)
    if num_set:
        return [max(num_set), min(num_set)]
    else:
        return [0,0]