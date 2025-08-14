from collections import deque

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
check = [[False] * M for _ in range(N)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    result = 1
    Q = deque()
    Q.append((y, x))
    while Q:
        ey, ex = Q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<M:
                if map[ny][nx] == 1 and check[ny][nx] == False:
                    result += 1
                    check[ny][nx] = True
                    Q.append((ny,nx))
    return result

count = 0
max_value = 0
for j in range(N):
    for i in range(M):
        if map[j][i] == 1 and check[j][i] == False:
            check[j][i] = True
            count += 1
            max_value = max(max_value, bfs(j,i))

print(count)
print(max_value)