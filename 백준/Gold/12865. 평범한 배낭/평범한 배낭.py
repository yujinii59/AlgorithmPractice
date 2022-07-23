n, k = map(int, input().split())
dp = {}
max_value = 0
for _ in range(n):
    w, v = map(int, input().split())
    dp_tmp = dp.copy()
    for wgt, val in dp_tmp.items():
        if wgt + w <= k:
            if wgt + w in dp:
                dp[wgt + w] = max(dp[wgt + w], val + v)
            else:
                dp[wgt + w] = val + v
            max_value = max(max_value, val + v)
    if w <= k:
        if w in dp:
            dp[w] = max(dp[w], v)
        else:
            dp[w] = v
        max_value = max(max_value, v)

print(max_value)
