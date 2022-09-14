from datetime import datetime
from math import ceil
def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    in_cars = {}
    cars_fee = {}
    for record in records:
        rec_time, number, rec = record.split()
        rec_time = datetime.strptime(rec_time, '%H:%M')
        if rec == 'IN':
            in_cars[number] = rec_time
        else:
            park_time = (rec_time - in_cars[number]).seconds // 60
            del in_cars[number]
            if cars_fee.get(number, 0):
                cars_fee[number] += park_time
            else:
                cars_fee[number] = park_time

    last_time = datetime.strptime('23:59', '%H:%M')
    for number, time in in_cars.items():
        park_time = (last_time - time).seconds // 60
        if cars_fee.get(number, 0):
            cars_fee[number] += park_time
        else:
            cars_fee[number] = park_time

    cars_fee = sorted(cars_fee.items())
    rst = []
    for number, time in cars_fee:
        fee = 0
        if time > base_time:
            time -= base_time
            fee += base_fee + (ceil(time / unit_time) * unit_fee)
        else:
            fee = base_fee
        rst.append(fee)
        
    return rst