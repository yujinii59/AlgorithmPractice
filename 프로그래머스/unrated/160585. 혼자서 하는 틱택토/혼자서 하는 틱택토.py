def solution(board):
    answer = 1
    victories = [
        [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]
    ]
    o = []
    x = []
    for i, row in enumerate(board):
        for j, state in enumerate(row):
            if state == 'O':
                o.append((i, j))
            elif state == 'X':
                x.append((i, j))
    len_o = len(o)
    len_x = len(x)
    if len_o < len_x or len_o > len_x + 1:
        answer = 0
    elif len_o == len_x:
        for victory in victories:
            if len(set(victory) - set(o)) == 0:
                answer = 0
                break
    else:
        for victory in victories:
            if len(set(victory) - set(x)) == 0:
                answer = 0
                break
            
    return answer