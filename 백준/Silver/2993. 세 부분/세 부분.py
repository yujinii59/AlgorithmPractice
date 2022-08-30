from itertools import combinations
string = input()
cases = combinations(list(range(1,len(string))), 2)
word = ''
for case in cases:
    f, s = case
    conv = string[:f][::-1] + string[f:s][::-1] + string[s:][::-1]
    if word == '':
        word = conv
    else:
        if word > conv:
            word = conv
print(word)