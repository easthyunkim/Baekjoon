import sys
input = sys.stdin.readline
K = int(input())
stack = []
for i in range(K):
    N = int(input())
    if stack and N == 0:
        stack.pop()
    else:
        stack.append(N)
print(sum(stack))