dp = [0]*(45+1)
for i in range(45+1):
    if i < 2:
        dp[i] = 1
        continue
    dp[i] = dp[i-1]+dp[i-2]
n = int(input())
for i in range(n):
    x = int(input())
    print(dp[x])