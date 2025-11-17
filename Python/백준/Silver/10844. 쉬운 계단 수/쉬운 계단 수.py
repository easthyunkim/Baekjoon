#2차원으로 확장한 점화식 문제
#a[N][K]=a[N−1][K−1]+a[N−1][K+1]

N = int(input()) #입력받기
dp = [[0]*10 for _ in range(N)] #DP 테이블 초기화
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] #초기값 설정

for n in range(1, N):
    dp[n][0] = dp[n-1][1] #끝자리가 0
    dp[n][9] = dp[n-1][8] #끝자리가 9
    for k in range(1, 9): #끝자리가 1~8
        dp[n][k] = dp[n-1][k-1] + dp[n-1][k+1]

print(sum(dp[N-1])%1000000000) #출력하기