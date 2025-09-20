import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

#입력 받기
n = int(input())
Ai = list(map(int, input().split()))
s = int(input())
v = [0]*(n+1)
cnt = 1

#dfs 정의하기
def dfs(x):
    global cnt
    for i in range(2):
        if not i:
            nx = x + Ai[x]
        else:
            nx = x - Ai[x]
        if 0 <= nx < n and not v[nx]:
            v[nx] = 1
            cnt += 1
            dfs(nx)

#출력하기
dfs(s-1)
print(cnt)