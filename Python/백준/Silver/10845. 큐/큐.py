import sys
N = int(sys.stdin.readline())
queue= []
def query() :
    Q = sys.stdin.readline().split()
    if Q[0] == 'push' :
        queue.append(int(Q[1]))
    if Q[0] == 'pop' :
        if len(queue) :
            print(queue.pop(0))
        else :
            print(-1)
    if Q[0] == 'size' :
        print(len(queue))
    if Q[0] == 'empty' :
        if len(queue) :
            print(0)
        else :
            print(1)
    if Q[0] == 'front' :
        if len(queue) :
            print(queue[0])
        else :
            print(-1)
    if Q[0] == 'back' :
        if len(queue) :
            print(queue[-1])
        else :
            print(-1)
for i in range (N) :
    query()