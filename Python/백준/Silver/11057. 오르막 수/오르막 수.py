N = int(input()) #입력받기
dp = [[0]*10 for _ in range(N+1)] #DP 테이블 초기화
dp[1] = [1]*10 #초기값 설정

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(sum(dp[N])%10007) #출력하기