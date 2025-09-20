import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    ans = 0
    for i in range(N):
        if i % 2 == 1:
            ans += i
    print(ans+N)