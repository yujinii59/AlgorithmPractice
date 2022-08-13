import sys
string = input()
ucpc = 'UCPC'
for s in ucpc:
    if string.find(s) >= 0:
        string = string[string.index(s)+1:]
    else:
        print('I hate UCPC')
        sys.exit()
print('I love UCPC')