from collections import Counter

def solution(weights):
    answer = 0
    rates = [1/2, 2/3, 3/4, 1, 4/3, 3/2, 2]
    counter = Counter(weights)
    for i, weight in enumerate(weights):
        counter[weight] -= 1
        # print(counter)
        for rate in rates:
            if counter.get(weight * rate, 0):
                answer += counter[weight*rate]
        
    return answer