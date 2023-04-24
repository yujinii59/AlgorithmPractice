def solution(name, yearning, photo):
    answer = []
    scores = {}
    for person, yearn in zip(name, yearning):
        scores[person] = yearn
        
    for picture in photo:
        score = 0
        for person in picture:
            score += scores.get(person, 0)
        answer.append(score)
    return answer