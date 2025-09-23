from heapq import heappop, heappush
import sys
input = sys.stdin.readline

#입력 받기
V, E = map(int, input().split())
K = int(input())
arr = [[]*(V+1) for _ in range(V+1)]
INF = float('INF')
dist = [INF]*(V+1)
for _ in range(E):
    U, V, W = map(int, input().split())
    arr[U].append((V, W))

#다익스트라 알고리즘
def dijkstra(S):
    Q= []
    heappush(Q, (0, S))
    dist[S] = 0

    while Q:
        D, V = heappop(Q)
        if dist[V] < D:
            continue

        for NV, NW in arr[V]:
            dist2 = D +NW
            if dist2 < dist[NV]:
                dist[NV] = dist2
                heappush(Q, (dist2, NV))

#출력하기
dijkstra(K)
for i in dist[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)