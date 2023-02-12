n = int(input())
string = input()
length = len(string) // n
direction = 1
rst = ['']*len(string)
for i in range(length):
    s = string[n*i:n*(i+1)][::direction]
    direction *= -1
    for j in range(n):
        rst[i + length*j] = s[j]
        
print(''.join(rst))