import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
cnt = 1

for i in arr:
    stack.append(i)
    while stack and stack[-1] == cnt:
            stack.pop()
            cnt += 1

if stack:
    print('Sad')
else:
    print('Nice')