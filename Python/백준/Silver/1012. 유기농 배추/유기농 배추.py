from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
dy = [0, 0, -1, 1]
dx = [-1, 1, -0, 0]

def bfs(gph, x, y) :
    Q = deque()
    Q.append([x, y])
    gph[x][y] = 0
    while Q :
        x, y = Q.popleft()
        for i in range (4) :
            ex = x + dx[i]
            ey = y + dy[i]
            if 0<=ex<M and 0<=ey<N and gph[ex][ey] == 1:
                Q.append([ex, ey])
                gph[ex][ey] = 0

for _ in range(T) :
    M, N, K = map(int, input().split())
    gph = [[0]*(N) for _ in range(M)]
    for _ in range (K) :
        A, B = map(int, input().split())
        gph[A][B] = 1
    
    cnt = 0
    for i in range(M) :
        for j in range(N) :
            if gph[i][j] == 1 :
                bfs(gph, i, j)
                cnt += 1
    print(cnt)