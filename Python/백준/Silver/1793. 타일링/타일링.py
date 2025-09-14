import sys
input = sys.stdin.readline

while True :
    try:
        N = int(input())
        dp = [1, 1, 3]

        for i in range(3, N+1):
           dp.append((dp[i-1] + dp[i-2]*2))
        print(dp[N])
    except :
        break