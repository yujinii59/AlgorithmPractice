n, m = map(int, input().split())
book = [(n, 0)]
max_page = 0
for _ in range(m):
    day, pages = map(int, input().split())
    tmp = book.copy()
    for res, page in tmp:
        if res >= day:
            book.append((res-day, page+pages))
            max_page = max(max_page, page+pages)
            
print(max_page)