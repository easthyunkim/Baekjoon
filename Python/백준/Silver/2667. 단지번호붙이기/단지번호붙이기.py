from collections import deque
import sys
input = sys.stdin.readline
dy = [0, 0, -1, 1]
dx = [-1, 1, -0, 0]

def bfs(gph, a, b):
    N = len(gph)
    Q = deque()
    Q.append([a, b])
    gph[a][b] = 0
    cnt = 1
    while Q:
        x, y = Q.popleft()
        for i in range (4):
            ex = x + dx[i]
            ey = y + dy[i]
            if ex < 0 or ex >= N or ey < 0 or ey >= N:
                continue
            if gph[ex][ey] == 1:
                gph[ex][ey] = 0
                Q.append([ex, ey])
                cnt += 1
    return cnt

N = int(input())
gph = []
for i in range(N):
    gph.append(list(map(int, input().rstrip())))

cnt = []
for i in range(N):
    for j in range(N):
        if gph[i][j] == 1:
            cnt.append(bfs(gph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])