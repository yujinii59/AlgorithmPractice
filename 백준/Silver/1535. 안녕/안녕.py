n = int(input())
dp = [(100, 0)]
healthes = list(map(int, input().split()))
pleasures = list(map(int, input().split()))
max_pleasure = 0
for health, pleasure in zip(healthes, pleasures):
    dp_tmp = dp.copy()
    for h, p in dp_tmp:
        if h > health:
            dp.append((h-health, p+pleasure))
            max_pleasure = max(max_pleasure, p+pleasure)
            
print(max_pleasure)