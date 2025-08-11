import sys
S = sys.stdin.readline().strip()+' '
stack = []
answer = ''
case = 0

for i in S :
    if i == '<' :
        case = 1
        for j in range(len(stack)) :
            answer += stack.pop()
    stack.append(i)

    if i == '>' :
        case = 0
        for j in range(len(stack)) :
            answer += stack.pop(0)

    if i == ' ' and case == 0 :
        stack.pop()
        for j in range(len(stack)) :
            answer += stack.pop()
        answer += ' '

print(answer)