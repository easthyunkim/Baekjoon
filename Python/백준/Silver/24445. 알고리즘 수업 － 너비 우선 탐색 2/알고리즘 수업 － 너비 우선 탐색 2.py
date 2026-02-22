from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
gph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 1

def bfs(gph, v, visited):
    global cnt
    queue = deque([v])
    visited[v] = cnt #방문 시 순서 세기
    while queue:
        v = queue.popleft()
        for i in gph[v]: #인접 정점 중
            if not visited[i]: #방문 안한 정점
                queue.append(i)
                cnt += 1
                visited[i] = cnt
            

for i in range(m):
    a, b = map(int, input().split())
    gph[a].append(b)
    gph[b].append(a) #양방향 간선

for i in range(n+1):
    gph[i].sort(reverse=True) #내림차순 정렬

bfs(gph, r, visited)

for i in range(1, n+1):
    print(visited[i])