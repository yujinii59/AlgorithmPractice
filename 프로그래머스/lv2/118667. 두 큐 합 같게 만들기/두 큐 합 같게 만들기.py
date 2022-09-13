from collections import deque

def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    if total % 2 == 1:
        rst = -1
    else:
        len1 = len(queue1)
        len2 = len(queue2)
        cnt = -1
        q1 = deque(queue1+queue2)
        q = deque()
        cnt1 = 0
        b = False
        summary = 0
        for i in range(len1+len2):
            if i >= len1:
                cnt1 += 1
            num = q1.popleft()
            q.append(num)
            summary += num
            while summary > total // 2:
                n = q.popleft()
                cnt1 += 1
                summary -= n

            if summary == total // 2:

                b = True
                if i < len1-1:
                    cnt1 += i+1 + len2
                break

        if b:
            cnt = cnt1

        q2 = deque(queue2+queue1)
        q = deque()
        cnt2 = 0
        b = False
        summary = 0
        for i in range(len1+len2):
            if i >= len2:
                cnt2 += 1
            num = q2.popleft()
            q.append(num)
            summary += num
            while summary > total // 2:
                n = q.popleft()
                cnt2 += 1
                summary -= n

            if summary == total // 2:
                b = True
                if i < len2-1:
                    cnt2 += i+1 + len1
                break
        if b:
            if cnt > 0:
                cnt = min(cnt, cnt2)
            else:
                cnt = cnt2
        rst = cnt
    return rst