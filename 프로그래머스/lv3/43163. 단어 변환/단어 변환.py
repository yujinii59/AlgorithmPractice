from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    length = len(begin)
    word_cases = {}
    for i in range(length):
        word_cases[i] = {}
        for word in words:
            cng = word[:i] + word[i+1:]
            ls = word_cases[i].get(cng, [])
            ls.append(word)
            word_cases[i][cng] = ls
    
    min_cnt = 0
    q = deque([(begin, 0, [])])
    while q:
        word, cnt, used = q.popleft()
        if word == target:
            min_cnt = cnt
            break
            
        for i in range(length):
            new = word[:i] + word[i+1:]
            ls = word_cases[i].get(new, [])
            for new_word in ls:
                if new_word not in used:
                    q.append((new_word, cnt+1, used+[new_word]))
        print(q)
            
    return min_cnt