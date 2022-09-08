words = ['pi','ka','chu']
s = input()
for word in words:
    s = s.replace(word, '-')

s = s.replace('-','')
if s == '':
    print('YES')
else:
    print('NO')