def sum_of_squares(num):
    if num == 0:
        return 0
    else:
        cnt = num
        for i in range(int(num**0.5), 0, -1):
            tmp = 1
            if lst[num-(i**2)] > 0:
                tmp += lst[num-(i**2)]
            else:
                tmp += sum_of_squares(num-(i**2))
            cnt = min(tmp, cnt)
        lst[num] = cnt
        return lst[num]
        

n = int(input())
lst = [0]*(n+1)
print(sum_of_squares(n))