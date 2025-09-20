import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
ans = [-1]*N
stack = [0]
F = Counter(A)

for i in range(N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        ans[stack.pop()] = A[i]
    stack.append(i)

print(*ans)