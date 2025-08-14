from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
Max = 100001
dis = [0]*Max

def bfs() :
    Q = deque()
    Q.append(N)
    while Q:
        x = Q.popleft()
        if x == K :
            print(dis[x])
            break
        for nx in (x-1, x+1, x*2) :
            if 0<=nx<Max and not dis[nx]:
                    dis[nx] = dis[x]+1
                    Q.append((nx))

bfs()