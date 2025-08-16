import sys
input = sys.stdin.readline

A = [i for i in range(1, 21)]
for i in range(10):
    M, N = map(int, input().split())
    M -= 1
    A[M:N] = A[M:N][::-1]
print(' '.join(map(str, A)))