import sys
input = sys.stdin.readline

dp = [0]*1000001 #DP테이블 초기화
dp = [0, 1, 2, 4, 7] #DP 결과값

for i in range(5, 11):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3]) #DP 작성하기

T = int(input())
for i in range(T):
    N = int(input())
    print(dp[N]) #테스트케이스 입력 및 출력하기