import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())
gph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    gph[a].append(b)
    gph[b].append(a)

def bfs(v):
    q = deque([v])
    cnt = 0
    visited[v] = True
    while q:
        v = q.popleft()
        for i in gph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt

print(bfs(1))