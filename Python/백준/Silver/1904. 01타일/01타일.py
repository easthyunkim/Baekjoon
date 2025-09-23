import sys
input = sys.stdin.readline

#입력받기
N = int(input())

#점화식 세우기 -> 피보나치 수열
dp = [0, 1, 2, 3]
for i in range(4, N+1):
    dp.append((dp[i-1] + dp[i-2])%15746)

#출력하기
print(dp[N])