import sys
sys.setrecursionlimit(1000000)

def dfs(graph, r, visited, seq):
    visited[r] = seq
    for i in graph[r]:
        if visited[i] == -1:
            visited = dfs(graph, i, visited, seq + 1)

    return visited


n, m, r = map(int, input().split())
graph = [[] for _ in range(n)]
visited = {i: -1 for i in range(n)}
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

for i in range(n):
    graph[i] = sorted(graph[i], reverse=True)

result = dfs(graph, r-1, visited, seq=0)
print(*result.values(), sep='\n')