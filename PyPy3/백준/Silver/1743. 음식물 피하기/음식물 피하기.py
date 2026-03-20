from collections import deque
import sys
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def bfs(gph, i, j):
    Q = deque()
    Q.append([i, j])
    gph[i][j] = 2 #visited
    result = 1
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            ex, ey = x+dx[k], y+dy[k]
            if 0<ex<=N and 0<ey<=M and gph[ex][ey] == 1:
                Q.append([ex, ey])
                gph[ex][ey] = 2
                result += 1
    return result

N, M, K = map(int, input().split())
gph = [[0]*(M+1) for _ in range(N+1)]
ans = 0
for _ in range (K):
    A, B = map(int, input().split())
    gph[A][B] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        if gph[i][j] == 1:
            answer = bfs(gph, i, j)
            ans = max(answer, ans)

print(ans)