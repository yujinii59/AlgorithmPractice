a, b = map(int, input().split())
press_button = abs(a-b)
n = int(input())
for _ in range(n):
    bookmark = int(input())
    press_button = min(press_button, 1+abs(bookmark-b))
    
print(press_button)