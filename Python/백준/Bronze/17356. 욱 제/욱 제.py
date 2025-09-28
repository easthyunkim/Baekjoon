import sys
input = sys.stdin.readline

#입력받기
A, B = map(int, input().split())

#M과 욱이 제를 이길 확률 계산
M = (B-A)/400
ans = 1/(1+10**M)

#출력하기
print(ans)