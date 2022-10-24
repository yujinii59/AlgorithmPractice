n = int(input())
waiting_line = []
line = list(map(int, input().split()))[::-1]
num = 1
while line or waiting_line:
    if line:
        seq_num = line.pop()
    else:
        seq_num = n+1
    if seq_num == num:
        num += 1
    else:
        if waiting_line:
            if waiting_line[-1] == num:
                line.append(seq_num)
                waiting_line.pop()
                num += 1
            else:
                if waiting_line[-1] < seq_num:
                    print('Sad')
                    break
                else:
                    waiting_line.append(seq_num)
        else:
            waiting_line.append(seq_num)
            
else:
    print('Nice')