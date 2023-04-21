def solution(spell, dic):
    spell = set(spell)
    answer = 2
    for word in dic:
        if len(spell) == len(word) and set(list(word)) == spell:
            answer = 1
            break
    return answer