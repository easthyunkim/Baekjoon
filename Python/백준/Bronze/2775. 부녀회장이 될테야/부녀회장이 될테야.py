import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    ans = [i for i in range(1, n+1)]

    for x in range(k):
        for y in range(1, n):
            ans[y] += ans[y-1]
    print(ans[-1])