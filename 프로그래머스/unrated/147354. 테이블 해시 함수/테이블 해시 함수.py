def solution(data, col, row_begin, row_end):
    data = sorted(data, key=lambda x: [x[col-1], -x[0]])
    prev_bit = 0
    for i in range(row_begin-1, row_end):
        row = data[i]
        total = 0
        for elem in row:
            total += elem % (i+1)
        
        curr_bit = int(bin(total)[2:])
        bit = str(prev_bit + curr_bit)
        tmp = ''
        for num in bit:
            if num == '2':
                tmp += '0'
            else:
                tmp += num
        prev_bit = int(tmp)
        print(prev_bit)
    return int(str(prev_bit), 2)