from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(a, b):
    Q = deque()
    Q.append((a, b))
    gph[a][b] = 0
    while Q:
        x, y = Q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < h and 0 <= ny < w and gph[nx][ny] == 1:
                Q.append((nx, ny))
                gph[nx][ny] = 0

while True:
    w, h = map(int, input().split())
    gph = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    if w == h == 0:
        break
    for i in range(h):
        for j in range(w):
            if gph[i][j] == 1:
                bfs(i, j)
                ans += 1
    print(ans)