elems = {'H':1, 'C':12, 'O':16}
formula = input()
way = 'p'
s = ['']
for e in formula:
    if e == '(':
        if way == 'a':
            s.append(s.pop()+s.pop())
        s.append('')
        way = 'p'
    elif e == ')':
        if way == 'a':
            s.append(s.pop()+s.pop())
        else:
            way = 'a'
    else:
        prev = s.pop()
        if e.isnumeric():
            if way == 'p':
                prev += prev[-1]*(int(e)-1)
            else:
                prev *= int(e)
                prev = s.pop()+prev
        else:
            if way == 'a':
                prev = s.pop()+prev
            prev += e
        s.append(prev)
        way = 'p'
rst =''.join(s)
total = 0
for symbol in rst:
    total += elems[symbol]
print(total)