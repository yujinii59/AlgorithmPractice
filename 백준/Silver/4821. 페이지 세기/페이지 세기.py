while True:
    last = int(input())
    if last == 0:
        break
    rngs = input().split(',')
    print_page = set()
    for rng in rngs:
        pages = rng.split('-')
        start = int(pages[0])
        end = min(int(pages[-1]), last)
        if start <= end:
            print_page = print_page | set(range(start, end+1))
    print(len(print_page))