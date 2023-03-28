def solution(keymap, targets):
    answer = []
    press_cnt = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            cnt = press_cnt.get(key, 999)
            if cnt > i+1:
                press_cnt[key] = i+1
    
    for target in targets:
        cnt = 0
        for key in target:
            if press_cnt.get(key, 0):
                cnt += press_cnt[key]
            else:
                cnt = -1
                break
        answer.append(cnt)
                
    return answer