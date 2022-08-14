money = int(input())
jun = sung = money
prices = list(map(int, input().split()))
stocks = {'jun': 0, 'sung': 0}
prev = prices[0]
state = '.'
cnt = 0
for price in prices:
    if jun >= price:
        stocks['jun'] += jun // price
        jun %= price

    if prev > price:
        if state != '+':
            cnt += 1
            state = '-'
        else:
            cnt = 1
            state = '-'
    elif prev < price:
        if state != '-':
            cnt += 1
            state = '+'
        else:
            cnt = 1
            state = '+'
    else:
        cnt = 0
        state = '.'

    if cnt >= 3:
        if state == '+':
            sung += price * stocks['sung']
            stocks['sung'] = 0
        elif state == '-':
            if sung >= price:
                stocks['sung'] += sung // price
                sung %= price

    prev = price

jun += prev * stocks['jun']
sung += prev * stocks['sung']

if jun > sung:
    print('BNP')
elif jun < sung:
    print('TIMING')
else:
    print('SAMESAME')