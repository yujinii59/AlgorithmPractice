from math import factorial

while True:
    try:
        string, num = input().split()
        num = int(num)
        l = len(string)
        if num > factorial(l):
            print(f'{string} {num} = No permutation')
        else:
            s = string
            n = num - 1
            make_string = ''
            for i in range(1, l+1):
                loc = n // factorial(l-i)
                n = n % factorial(l-i)
                make_string += s[loc]
                s = s[:loc]+s[loc+1:]
            print(f'{string} {num} = {make_string}')
    except:
        break