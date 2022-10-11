def calc_fibonacci(num):
    fibo = [0,0]
    for i in range(num+1):
        if i == 0:
            fibo[1] = 0
        elif i == 1:
            fibo[0] = fibo[1]
            fibo[1] = 1
        else:
            fibo[0], fibo[1] = fibo[1], (fibo[0] + fibo[1]) % 1000000000
#         print(i,fibo[1])

    return fibo[1]
            

n = int(input())
if n < 0:
    sign = -1
else:
    sign = 1
    
rst = calc_fibonacci(abs(n))
if n % 2 == 0:
    rst *= sign
if rst < 0:
    print(-1)
elif rst == 0:
    print(0)
else:
    print(1)
    
print(abs(rst)%1000000000)