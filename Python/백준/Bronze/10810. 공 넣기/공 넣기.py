import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [0]*N

for _ in range(M):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        basket[l]=k

for x in range(N):
    print(basket[x], end=' ')