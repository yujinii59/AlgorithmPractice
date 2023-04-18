def solution(n, lighthouse):
    answer = 0
    conn = {}
    roads = {}
    for n1, n2 in lighthouse:
        roads[n1] = roads.get(n1, 0) + 1
        roads[n2] = roads.get(n2, 0) + 1
        n1_conn = conn.get(n1, set())
        n1_conn.add(n2)
        n2_conn = conn.get(n2, set())
        n2_conn.add(n1)
        conn[n1] = n1_conn
        conn[n2] = n2_conn
    
    while sum(roads.values()) > 0:
        light_set = set()
        for num, cnt in roads.items():
            if cnt == 1:
                for n in conn[num]:
                    light_set.add(n)
                
        for num in light_set:
            if roads[num]:
                answer += 1
                roads[num] = 0
                for n in conn[num]:
                    conn[n].discard(num)
                    roads[n] -= 1
    return answer