import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2] #피보나치 수열과 동일함

print(dp[N])