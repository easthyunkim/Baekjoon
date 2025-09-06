import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]
A = 0

for _ in range(M):
    i, j = map(int, input().split())
    A= basket[i-1:j]
    A.reverse()
    basket[i-1:j] = A

for x in range(N):
    print(basket[x], end=' ')