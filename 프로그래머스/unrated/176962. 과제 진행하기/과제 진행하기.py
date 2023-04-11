def solution(plans):
    plans = sorted(plans, key=lambda x: x[1])
    answer = []
    res = []
    end = 0
    for subject, t, m in plans:
        hour, minute = map(int, t.split(":"))
        time = hour * 60 + minute
        while res:
            sj, res_time = res.pop()
            if end + res_time <= time:
                answer.append(sj)
                end += res_time
            else:
                res.append((sj, res_time - (time - end)))
                break
        res.append((subject, int(m)))
        end = time

    while res:
        subject, _ = res.pop()
        answer.append(subject)

    return answer