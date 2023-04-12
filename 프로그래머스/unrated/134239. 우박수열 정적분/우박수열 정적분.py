def solution(k, ranges):
    heights = [k]
    while k > 1:
        if k % 2:
            k = 3 * k + 1
            
        else:
            k //= 2
        heights.append(k)

    length = len(heights)-1
    answer = []
    for start, end in ranges:
        end += length
        if start > end:
            answer.append(-1)
        else:
            total = 0
            for i in range(start, end):
                total += (heights[i] + heights[i+1]) / 2
            answer.append(total)
            
    
    return answer