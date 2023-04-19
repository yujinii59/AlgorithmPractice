def solution(triangle):
    answer = 0
    results = []
    for i, nums in enumerate(triangle):
        tmp = []
        for j, num in enumerate(nums):
            max_num = num
            if j - 1 >= 0:
                max_num = max(max_num, results[j-1] + num)
            if j < i:
                max_num = max(max_num, results[j] + num)
                
            tmp.append(max_num)
        results = tmp
                
            
    return max(results)