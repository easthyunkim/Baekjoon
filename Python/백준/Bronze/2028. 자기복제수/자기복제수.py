import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    num = int(input())
    k = len(str(num))
    if str(num**2)[-k:] == str(num):
        print("YES")
    else:
        print("NO")