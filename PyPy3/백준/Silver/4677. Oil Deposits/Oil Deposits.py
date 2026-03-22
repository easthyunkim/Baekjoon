from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(a, b):
    Q = deque()
    Q.append((a, b))
    gph[a][b] = '*'
    while Q:
        x, y = Q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and gph[nx][ny] != '*':
                Q.append((nx, ny))
                gph[nx][ny] = '*'

while True:
    m, n = map(int, input().split())
    gph = [list(input()) for _ in range(m)]
    ans = 0
    if m == n == 0:
        break
    for i in range(m):
        for j in range(n):
            if gph[i][j] == '@':
                bfs(i, j)
                ans += 1
    print(ans)