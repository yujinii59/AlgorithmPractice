strings = input()
is_not_tag = True
string = ''
tag = ''
for s in strings:
    if s == '<':
        print(string[::-1], end='')
        string = ''
        is_not_tag = False
        tag += s
        continue
    elif s == '>':
        is_not_tag = True
        tag += s
        print(tag, end='')
        tag = ''
        continue
    if is_not_tag:
        if s == ' ':
            print(string[::-1] + ' ', end='')
            string = ''
        else:
            string += s
    else:
        tag += s
print(string[::-1])