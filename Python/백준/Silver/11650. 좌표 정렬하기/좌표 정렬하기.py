import sys
input = sys.stdin.readline

N = int(input())
user = []
for i in range(N):
    x, y = input().split()
    user.append([int(x), int(y)]) #입력받기

for i in sorted(user):
    print(i[0], i[1]) #출력하기