import sys
input = sys.stdin.readline

N = int(input())
ans = []
for i in range(N):
    x, y = input().split()
    ans.append([int(x), int(y)]) #입력받기

for i in sorted(ans, key = lambda x: (x[1], x[0])):
    print(i[0], i[1]) #출력하기