from collections import deque
import sys
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(a, b):
    sheep = 0
    wolf = 0
    Q = deque()
    Q.append((a, b))
    if gph[a][b] == 'o':
        sheep += 1
    elif gph[a][b] == 'v':
        wolf += 1
    gph[a][b] = '#'
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x+dx[i] 
            ny = y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and gph[nx][ny] != '#':
                if gph[nx][ny] == 'o':
                    sheep += 1
                elif gph[nx][ny] == 'v':
                    wolf += 1
                gph[nx][ny] = '#'
                Q.append((nx, ny))
    if wolf >= sheep:
        return 0, wolf
    elif sheep > wolf:
        return sheep, 0

r, c = map(int, input().split())
total_sheep = 0
total_wolf = 0
gph = [list(input()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if gph[i][j] in 'ov':
            result_sheep, result_wolf = bfs(i, j)
            total_sheep += result_sheep
            total_wolf += result_wolf

print(total_sheep, total_wolf)