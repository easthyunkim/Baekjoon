import sys
T = int(sys.stdin.readline())
for i in range(T) :
    N = sys.stdin.readline()
    stack = []
    for j in N :     
        if j == '(' :
            stack.append('(')
        elif j == ')' :
            if len(stack) == 0 :
                stack.append(')')
                break
            else :
                stack.pop()
    if len(stack)!=0 :
        print('NO')
    else :
        print('YES')