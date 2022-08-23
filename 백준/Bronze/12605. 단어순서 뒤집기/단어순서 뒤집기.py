n = int(input())
for i in range(n):
    string = input().split()
    print(f"Case #{i+1}: {' '.join(string[::-1])}")