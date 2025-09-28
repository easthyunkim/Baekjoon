import sys
input = sys.stdin.readline

#입력받기
N = int(input())

#팩토리얼 계산하기
ans = 1
for i in range(2, N+1):
    ans *= i

#출력하기
print(int(ans/60/60/24/7))