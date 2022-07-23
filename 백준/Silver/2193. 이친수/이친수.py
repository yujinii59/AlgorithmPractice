def fibonacci(num):
    if num <= 2:
        fibo[num] = 1
    else:
        fibo[num] = fibo[num-1] + fibo[num-2]
        

n = int(input())
fibo = [0 for _ in range(n+1)]
for i in range(1, n+1):
    fibonacci(i)
print(fibo[n])