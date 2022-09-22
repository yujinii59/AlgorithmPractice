from itertools import combinations

def solution(orders, course):
    menus = {c:{} for c in course}
    for order in orders:
        l = len(order)
        order = sorted(order)
        for n in course:
            if n <= l:
                cases = set(combinations(order, n))
                for case in cases:
                    case = ''.join(case)
                    if menus[n].get(case, 0):
                        menus[n][case] += 1
                        
                    else:
                        menus[n][case] = 1
    
    rst = []
    for c, comb in menus.items():
        prev = 2
        for menu, cnt in sorted(comb.items(), key=lambda x:[-x[1], x[0]]):
            if cnt >= prev:
                rst.append(menu)
                prev = cnt
            else:
                break
        
    return sorted(rst)
                
                