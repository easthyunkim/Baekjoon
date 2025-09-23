from heapq import heappop, heappush
import sys
input = sys.stdin.readline

#입력 받기
N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    U, V, W = map(int, input().split())
    arr[U].append((V, W))
S, E = map(int, input().split())

#다익스트라 알고리즘
INF = float('INF')
dist = [INF]*(N+1)

def dijkstra(S):
    visited = [False]*(N+1)
    Q = [(0, S)]
    dist[S] = 0

    while Q:
        D, V = heappop(Q)
        if visited[V]:
            continue

        visited[V] = True
        for NV, NW in arr[V]:
            dist2 = D +NW
            if dist2 < dist[NV]:
                dist[NV] = dist2
                heappush(Q, (dist2, NV))

#출력하기
dijkstra(S)
print(dist[E])