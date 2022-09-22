import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = ''.join(re.findall(r'[a-z0-9.\-_]+', new_id))
    prev = '.'
    tmp = ''
    for s in new_id:
        if s == prev and prev == '.':
            continue
        tmp += s
        prev = s
    new_id = tmp
    
    if prev == '.':
        new_id = new_id[:-1]
        
    l = len(new_id)
    if l == 0:
        new_id = 'a'
        l = 1
    if l >= 16:
        target = 15
        if new_id[14] == '.':
            target -= 1
        new_id = new_id[:target]
        l = target
    
    if l <= 2:
        last_str = new_id[-1]
        new_id = new_id + last_str*(3-l)
        
    return new_id
        