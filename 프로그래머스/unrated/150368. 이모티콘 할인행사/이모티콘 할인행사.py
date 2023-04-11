from itertools import product

def solution(users, emoticons):
    cases = product([10,20,30,40], repeat=len(emoticons))
    max_plus = 0
    max_price = 0
    for case in cases:
        discount_prices = []
        for rate, price in zip(case, emoticons):
            discount_prices.append((rate, price*(100-rate)//100))

        plus_cnt = 0
        emoticon_price = 0
        for min_rate, min_price in users:
            total = 0
            for rate, price in discount_prices:
                if min_rate <= rate:
                    total += price
            if total >= min_price:
                plus_cnt += 1
            else:
                emoticon_price += total

        if plus_cnt > max_plus:
            max_plus = plus_cnt
            max_price = emoticon_price
        elif plus_cnt == max_plus and emoticon_price > max_price:
            max_price = emoticon_price

    answer = [max_plus, max_price]
    return answer