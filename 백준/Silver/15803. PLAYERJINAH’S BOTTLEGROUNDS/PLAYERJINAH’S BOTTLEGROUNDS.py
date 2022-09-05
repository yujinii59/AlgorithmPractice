x, y = map(int, input().split())
div = set()
for _ in range(2):
    a, b = map(int, input().split())
    if x == a:
        div.add('inf')
    else:
        div.add((y-b)/(x-a))
        
    x, y = a, b

if len(div) == 1:
    print('WHERE IS MY CHICKEN?')
else:
    print('WINNER WINNER CHICKEN DINNER!')