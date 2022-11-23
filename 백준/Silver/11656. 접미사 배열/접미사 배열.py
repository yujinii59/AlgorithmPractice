string = input()
ls = sorted([string[i:] for i in range(len(string))])
print(*ls, sep='\n')