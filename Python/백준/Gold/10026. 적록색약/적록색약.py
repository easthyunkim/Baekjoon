import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def dfs(gph, visited, i, j):
    visited[i][j] = 1
    for k in range(4):
        ex, ey = i+dx[k], j+dy[k]
        if 0 <= ex < N and 0 <= ey < N:
            if gph[i][j] == gph[ex][ey] and visited[ex][ey] == 0:
                dfs(gph, visited, ex, ey)

N = int(input())
gph = [list(input().strip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
ans1, ans2 = 0, 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(gph, visited, i, j)
            ans1 += 1

for i in range(N):
    for j in range(N):
        if gph[i][j] == 'G':
            gph[i][j] = 'R'

visited_2 = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited_2[i][j]:
            dfs(gph, visited_2, i, j)
            ans2 += 1

print(ans1, ans2)