from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
#상하좌우뿐만 아니라 대각선까지 8방향을 고려하여야 하는 문제
def bfs(a, b):
    Q = deque()
    Q.append((a, b))
    gph[a][b] = '.'
    while Q:
        x, y = Q.popleft()
        for i in range(8): #8방향이므로 4 -> 8
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and gph[nx][ny] == '#':
                Q.append((nx, ny))
                gph[nx][ny] = '.'

m, n = map(int, input().split())
gph = [list(input()) for _ in range(m)]
cnt = 0
for i in range(m):
    for j in range(n):
        if gph[i][j] == '#':
            bfs(i, j)
            cnt += 1
print(cnt)