from heapq import heappop, heappush
import sys
input = sys.stdin.readline

#입력 받기
A = lambda : map(int, input().split())
N, M, X = A()
arr = [[] for _ in range(N+1)]
INF = float('INF')
for _ in range(M):
    U, V, T = A()
    arr[U].append((V, T))

#다익스트라 알고리즘
def dijkstra(S):
    dist = [INF]*(N+1)
    dist[S] = 0
    Q= [(0, S)]

    while Q:
        D, V = heappop(Q)
        if dist[V] < D:
            continue

        for NV, NW in arr[V]:
            dist2 = D + NW
            if dist2 < dist[NV]:
                dist[NV] = dist2
                heappush(Q, (dist2, NV))
    return dist

#출력하기
ans = [[]]
for i in range(1, N+1):
    ans.append(dijkstra(i))

result = 0
for i in range(1, N+1):
    result = max(result, ans[i][X] + ans[X][i])
print(result)