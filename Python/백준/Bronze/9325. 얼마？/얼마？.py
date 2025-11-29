import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    s = int(input())
    n = int(input())
    ans = s

    for _ in range(n):
        q, p = map(int, input().split())
        ans += q*p
    print(ans)