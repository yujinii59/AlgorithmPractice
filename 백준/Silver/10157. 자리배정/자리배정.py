c, r = map(int, input().split())
k = int(input())
def find_location(col, row, start, target, i):
    outer = 2*(col+row)-4
    answer = [0,0]
    if target < start + outer:
        if row == 1:
            answer = [i+(target-start), i]
        elif col == 1:
            answer = [i, i+(target-start)]
        else:
            if target < start + row:
                answer = [i, i+target-start]
            elif target < start + row + col-1:
                answer = [i+(target-(start+row-1)), i+row-1]
            elif target < start + 2*row + col-2:
                answer = [i+col-1, i+row-1 - (target-(start+row+col-2))]
            else:
                answer = [i+col-1-(target-(start+2*row+col-3)), i]
    else:
        answer =  find_location(col-2, row-2, start+outer, target, i+1)
        
    return answer

if k > c*r:
    print(0)
else:
    print(*find_location(c, r, 1, k, 1))
        