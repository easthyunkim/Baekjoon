from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
gph = []
for _ in range(N) :
     gph.append(list(map(int, input().rstrip())))

dy = [0,1,0,-1]
dx = [1,0,-1,0]
cnt = 0
def bfs(y, x) :
    Q = deque()
    Q.append((y, x))
    while Q:
        y, x = Q.popleft()
        for k in range(4) :
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<N and 0<=nx<M and gph[ny][nx] == 1 :
                    Q.append((ny,nx))
                    gph[ny][nx] = gph[y][x] + 1
    return gph[N-1][M-1]

print(bfs(0, 0))