import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    stack.append(int(input()))
last = stack[-1]
ans = 1
for i in reversed(range(N)):
    if stack[i] > last:
        ans += 1
        last = stack[i]

print(ans)