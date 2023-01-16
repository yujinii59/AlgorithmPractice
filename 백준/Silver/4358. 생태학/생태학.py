import sys

input = sys.stdin.readline

trees = {}
total = 0
while True:
    name = input().strip()
    if name:
        cnt = trees.get(name, 0)
        trees[name] = cnt + 1
        total += 1
    else:
        break

trees = sorted(trees.items())
for tree, cnt in trees:
    print(f'{tree} {(cnt / total) * 100:.4f}')