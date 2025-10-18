import sys
input = sys.stdin.readline

A, B = map(int, input().split()) #입력받기
ans = 0

if A == B+1: #같을 경우 만들 수 있음
    ans = A+B
elif A > B+1: #치즈의 개수만큼만
    ans = (B+1)+B
elif A < B+1: #패티의 개수만큼만
    ans = A+(A-1)

print(ans) #출력하기