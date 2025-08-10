import sys
N = int(sys.stdin.readline())
stack = []
def query() :
    Q = sys.stdin.readline().split()
    if Q[0] == 'push' :
        stack.append(int(Q[1]))
    if Q[0] == 'pop' :
        if len(stack) :
            print(stack.pop())
        else :
            print(-1)
    if Q[0] == 'size' :
        print(len(stack))
    if Q[0] == 'empty' :
        if len(stack) :
            print(0)
        else :
            print(1)
    if Q[0] == 'top' :
        if len(stack) :
            print(stack[-1])
        else :
            print(-1)
for i in range (N) :
    query()