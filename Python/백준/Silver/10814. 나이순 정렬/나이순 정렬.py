import sys
input = sys.stdin.readline

N = int(input())
user = []
for i in range(N):
    age, name = input().split()
    user.append([int(age), name]) #입력받기

for i in sorted(user, key=lambda x:x[0]):
    print(i[0], i[1]) #출력하기