n, m = map(int, input().split())
teams = {}
member_of_team = {}
for _ in range(n):
    team = input()
    c = int(input())
    teams[team] = []
    for _ in range(c):
        member = input()
        teams[team].append(member)
        member_of_team[member] = team

for _ in range(m):
    name = input()
    kind = int(input())
    if kind == 1:
        print(member_of_team[name])
    else:
        print(*sorted(teams[name]), sep='\n')