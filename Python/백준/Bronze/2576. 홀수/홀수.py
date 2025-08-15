import sys
input = sys.stdin.readline

ans = []

for i in range(7):
    N = int(input())
    if N % 2 == 1:
        ans.append(N)

if ans == [] :
    print(-1)
else :
    print(sum(ans))
    print(min(ans))