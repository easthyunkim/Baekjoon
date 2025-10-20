import sys
input = sys.stdin.readline

N = int(input())
X, S = map(int, input().split())
attack = 0
sign = False

for i in range(N):
    C, P = map(int, input().split()) #입력받기
    if C <= X and S < P:
        sign = True
        break

if sign:
    print('YES')
else:
    print('NO') #출력하기