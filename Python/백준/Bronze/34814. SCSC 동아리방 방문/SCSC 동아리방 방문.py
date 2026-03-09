import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(M):
    l, h = map(int, input().split())
    l -= 1
    h -= 1
    max_cnt = max(A)

    if A[h] == max_cnt:
        continue
    A[l] -= 1

print(*A)