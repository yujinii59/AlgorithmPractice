def solution(wallpaper):
    answer = [100,100,0,0]
    for i, row in enumerate(wallpaper):
        for j, file in enumerate(row):
            if file == '#':
                if answer[0] > i:
                    answer[0] = i
                if answer[2] < i+1:
                    answer[2] = i+1
                if answer[1] > j:
                    answer[1] = j
                if answer[3] < j+1:
                    answer[3] = j+1
    return answer