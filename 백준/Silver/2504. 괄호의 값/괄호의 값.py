string = input()
par = []
b = True
result = ''
prev = ''
for s in string:
    i = len(result)
    if s == '(' or s == '[':
        if prev == ')' or prev == ']':
            result = result[:-1] + '+('
        else:
            result += '('
        par.append((i, s))
    elif s == ')':
        if len(par) == 0:
            b = False
            break
        loc, ss = par.pop()
        if ss != '(':
            b = False
            break
        else:
            if result[-1] == '(':
                result += '2)*'
            else:
                tmp = result[-1]
                result = result[:-1] + ')' 
                result = result[:loc] + '(' + str(int(eval(result[loc:]))) + tmp + '2)*'
    elif s == ']':
        if len(par) == 0:
            b = False
            break
        loc, ss = par.pop()
        if ss != '[':
            b = False
            break
        else:
            if result[-1] == '(':
                result += '3)*'
            else:
                tmp = result[-1]
                result = result[:-1] + ')'
                result = result[:loc] + '(' + str(int(eval(result[loc:]))) + tmp + '3)*'
    
    else:
        b = False
        break
    prev = s

if len(par) > 0:
    b = False
                
if b:
    print(int(eval(result[:-1])))
else:
    print(0)