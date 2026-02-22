from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
gph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

def bfs(gph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in gph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(gph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in gph[v]:
        if not visited[i]: 
            dfs(gph, i, visited)

for i in range(m):
    a, b = map(int, input().split())
    gph[a].append(b)
    gph[b].append(a)

for i in range(n+1):
    gph[i].sort()

dfs(gph, r, visited)
visited = [False]*(n+1)
print()
bfs(gph, r, visited)