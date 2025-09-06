import sys
input = sys.stdin.readline

N = int(input())
dp = [0, 1, 3, 5]

for i in range(4, 1000+1):
    dp.append((dp[i-1] + (dp[i-2]*2))%10007)

print(dp[N])