S = input()

stack = []
cnt = 0
for i in range(len(S)):
    if S[i] == '(':
        stack.append(S[i])
    else:
        stack.pop()
        if S[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)