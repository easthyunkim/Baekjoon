import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(gph, v, visited):
    visited[v] = True
    for i in gph[v]:
        if not visited[i]:
            dfs(gph, i, visited)

n, m = map(int, input().split())
gph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    gph[u].append(v)
    gph[v].append(u)

cnt = 0
visited = [False]*(n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(gph, i, visited)
        cnt += 1

print(cnt)