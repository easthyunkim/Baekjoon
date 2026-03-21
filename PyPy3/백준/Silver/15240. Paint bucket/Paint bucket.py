from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(a, b, k):
    Q = deque()
    Q.append((a, b))
    n = gph[a][b]
    visited[a][b] = 1
    gph[a][b] = k
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and gph[nx][ny] == n and not visited[nx][ny]:
                gph[nx][ny] = k
                visited[nx][ny] = 1
                Q.append((nx, ny))

r, c = map(int, input().split())
gph = [list(input().rstrip()) for _ in range(r)]
x, y, k = map(int, input().split())
visited = [[0]*c for _ in range(r)]

bfs(x, y, str(k))
for i in gph:
    print(''.join(i))