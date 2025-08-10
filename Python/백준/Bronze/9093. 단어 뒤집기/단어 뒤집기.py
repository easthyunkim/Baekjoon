import sys
T = int(sys.stdin.readline())
for i in range(T) :
    S = sys.stdin.readline().split()
    for j in S :
        print(j[::-1], end=' ')