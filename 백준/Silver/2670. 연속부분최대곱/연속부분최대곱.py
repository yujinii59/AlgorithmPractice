n = int(input())
max_prev = 0
max_mult = 0
for _ in range(n):
    number = float(input())
    mult = max_prev * number
    max_prev = max(number, mult)
    max_mult = max(max_mult, max_prev)
print(f'{max_mult:.3f}')