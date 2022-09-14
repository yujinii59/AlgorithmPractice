n = int(input())
students = [input() for _ in range(n)]
succ = False
for i in range(len(str(n)), len(students[0])+1):
    if succ:
        i -= 1
        break
    succ = True
    num = set()
    for student in students:
        number = student[-i:]
        if number in num:
            succ = False
            break
        num.add(number)

print(i)