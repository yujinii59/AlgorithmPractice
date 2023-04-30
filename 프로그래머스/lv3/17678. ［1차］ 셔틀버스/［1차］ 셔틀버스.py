def solution(n, t, m, timetable):
    answer = ''
    conv_timetable = []
    for time in timetable:
        h, minute = time.split(":")
        minutes = int(h) * 60 + int(minute)
        conv_timetable.append(minutes)
    conv_timetable.sort()
    start = 9*60
    last_time = 0
    cnt = 0
    for conv in conv_timetable:
        if conv <= start:
            if cnt == m:
                if n > 1:
                    start += t
                    n -= 1
                    cnt = 1
                else:
                    break
            else:
                cnt += 1
            last_time = conv
        else:        
            while conv > start:
                if n <= 1:
                    n -= 1
                    break
                start += t
                n -= 1
                cnt = 0

            else:
                cnt = 1
                last_time = conv
        
            if n < 1:
                break
                
    if start >= last_time:
        if cnt < m:
            q, r = divmod(start, 60)
            answer = str(q).zfill(2) + ':' + str(r).zfill(2)
        elif cnt == m:
            q, r = divmod(last_time-1, 60)
            answer = str(q).zfill(2) + ':' + str(r).zfill(2)
    
            
        
    return answer