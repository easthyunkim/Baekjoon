import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque([])
def query() :
    Q = sys.stdin.readline().strip().split()
    if Q[0] == 'push_front' :
        queue.appendleft(int(Q[1]))
    if Q[0] == 'push_back' :
        queue.append(int(Q[1]))
    if Q[0] == 'pop_front' :
        if len(queue) :
            print(queue.popleft())
        else :
            print(-1)
    if Q[0] == 'pop_back' :
        if len(queue) :
            print(queue.pop())
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