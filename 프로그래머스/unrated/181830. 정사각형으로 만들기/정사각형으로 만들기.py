def solution(arr):
    r = len(arr)
    c = len(arr[0])
    if r > c:
        add = [0]*(r-c)
        for i in range(r):
            arr[i] += add
    elif r < c:
        add = [0]*c
        for _ in range(c-r):
            arr.append(add)
    return arr