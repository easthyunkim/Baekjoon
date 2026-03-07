import sys
input = sys.stdin.readline

N = int(input())
ans = 0
v1 = [0]*N
v2 = [0]*(2*N)
v3 = [0]*(2*N)
def dfs(i):
    global ans
    if i == N: #N행 까지 진행한 경우 경우의 수 가능
        ans += 1
        return
    for j in range(N):
        if v1[j] == v2[i+j] == v3[i-j] == 0: #열/대각선 모두 Queen X
            v1[j] = v2[i+j] = v3[i-j] = 1
            dfs(i+1)
            v1[j] = v2[i+j] = v3[i-j] = 0
dfs(0)
print(ans)