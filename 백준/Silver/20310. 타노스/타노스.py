s = list(map(int, list(input())))
half = [s.count(0)//2, s.count(1)//2]
cnts = [0,0]
pass_one = 0
string = ''
for ss in s:
    if ss == 1 and pass_one < half[1]:
        pass_one += 1
    else:
        if cnts[ss] < half[ss]:
            cnts[ss] += 1
            string += str(ss)
print(string)