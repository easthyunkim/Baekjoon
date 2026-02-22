import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
gph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 1

def dfs(gph, v, visited):
    global cnt
    visited[v] = cnt #방문 시 순서 세기
    for i in gph[v]:
        if not visited[i]:
            cnt += 1 #방문 안한 정점
            dfs(gph, i, visited)

for i in range(m):
    a, b = map(int, input().split())
    gph[a].append(b)
    gph[b].append(a) #양방향 간선

for i in range(n+1):
    gph[i].sort() #오름차순 정렬

dfs(gph, r, visited)

for i in range(1, n+1):
    print(visited[i])