import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    M = input().split()
    if M[0] == '1':
        stack.append(int(M[1]))
    if M[0] == '2':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    if M[0] == '3':
        print(len(stack))
    if M[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    if M[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)