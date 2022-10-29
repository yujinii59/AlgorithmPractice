rel = {'K':'S', 'R':'L'}
pre_skill = {'S':0, 'L':0}
n = int(input())
skills = input()
cnt = 0
for skill in skills:
    if skill in ['S','L']:
        pre_skill[skill] += 1
    elif skill in ['K','R']:
        if pre_skill[rel[skill]] > 0:
            cnt += 1
            pre_skill[rel[skill]] -= 1
        else:
            break
    else:
        cnt += 1
print(cnt)