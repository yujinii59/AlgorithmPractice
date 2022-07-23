n, m = map(int, input().split())
whole_strings = 1000
each_of_strings = 1000
for _ in range(m):
    whole, each = map(int, input().split())
    whole_strings = min(whole_strings, whole)
    each_of_strings = min(each_of_strings, each)

if whole_strings < each_of_strings * 6:
    money = whole_strings * (n // 6)
    if whole_strings < each_of_strings * (n % 6):
        money += whole_strings
    else:
        money += each_of_strings * (n % 6)
else:
    money = each_of_strings * n
    
print(money)
