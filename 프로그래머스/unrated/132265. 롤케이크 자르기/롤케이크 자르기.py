from collections import Counter

def solution(topping):
    answer = 0
    counter = Counter(topping)
    divide = dict()
    for num in topping:
        cnt = divide.get(num, 0)
        divide[num] = cnt + 1
        if counter[num] > 1:
            counter[num] -= 1
        else:
            del counter[num]
        
        if len(divide) == len(counter):
            answer += 1
    return answer