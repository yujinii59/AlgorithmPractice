def solution(s):
    answer = 0
    first = ''
    cnts = [0,0]
    for string in s:
        if first == '':
            answer += 1
            first = string
            cnts[0] += 1
        elif string == first:
            cnts[0] += 1
        else:
            cnts[1] += 1
            
        if cnts[0] == cnts[1]:
            first = ''
            cnts = [0,0]
    return answer