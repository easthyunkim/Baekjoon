#학습을 위해 참고한 블로그
#https://velog.io/@falling_star3/백준Python-1260번-DFS와BFS

import sys
from collections import deque

#입력 받기
n, m ,v = map(int, input().split())
gph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

#DFS 정의하기
def dfs(n):
    visited[n] = True
    print(n, end=' ')
    for i in gph[n]:
        if not visited[i]:
            dfs(i)

#bfs 정의하기
def bfs(n):
    visited[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in gph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

#인접리스트 만들기
for i in range(m):
    a, b = map(int, input().split())
    gph[a].append(b)
    gph[b].append(a)

#인접리스트 정렬
for i in range(1, n+1):
    gph[i].sort()

#출력, 체크리스트 초기화
dfs(v)
visited = [False]*(n+1)
print()
bfs(v)