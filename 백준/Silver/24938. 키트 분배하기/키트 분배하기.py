n = int(input())
kits = list(map(int, input().split()))
per = sum(kits) // n
shortage = {}
surplus = {}
congestion = 0
for i, kit in enumerate(kits):
    if kit < per:
        rst = per-kit
        surplus_tmp = surplus.copy()
        for loc, num in surplus_tmp.items():
            if rst:
                if num <= rst:
                    congestion += abs(loc - i) * num
                    del surplus[loc]
                    rst -= num
                else:
                    congestion += abs(loc-i) * rst
                    surplus[loc] -= rst
                    rst = 0
            else:
                break
        if rst > 0:
            shortage[i] = rst
    elif kit > per:
        rst = kit-per
        shortage_tmp = shortage.copy()
        for loc, num in shortage_tmp.items():
            if rst:
                if num <= rst:
                    congestion += abs(loc - i) * num
                    del shortage[loc]
                    rst -= num
                else:
                    congestion += abs(loc-i) * rst
                    shortage[loc] -= rst
                    rst = 0
            else:
                break
        if rst > 0:
            surplus[i] = rst
        
print(congestion)
                