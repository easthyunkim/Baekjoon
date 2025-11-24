import sys
input = sys.stdin.readline

ans = 0

N = int(input())
for i in range(N):
    A, B, C = map(int, input().split())
    if A == B == C:
        ans = max(ans, 10000+(A*1000))
    elif A == B:
        ans = max(ans, 1000+(A*100))
    elif B == C:
        ans = max(ans, 1000+(B*100))
    elif C == A:
        ans = max(ans, 1000+(A*100))
    else:
        ans = max(ans, max(A, B, C)*100)

print(ans)