from itertools import permutations

n = int(input())
inp = list(map(int, input().split()))
cases = permutations(inp, n)

max_ans = 0
for case in cases:
    ans = 0
    for i in range(n-1):
        ans += abs(case[i]-case[i+1])
#         print(abs(arr[i]-arr[i+1]), ans)
#     print(ans)
    max_ans = max(max_ans, ans)
print(max_ans)