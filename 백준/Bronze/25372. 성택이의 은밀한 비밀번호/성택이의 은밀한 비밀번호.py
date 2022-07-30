n = int(input())

for _ in range(n):
    string = input()
    if 6 <= len(string) <= 9:
        print('yes')
    else:
        print('no')