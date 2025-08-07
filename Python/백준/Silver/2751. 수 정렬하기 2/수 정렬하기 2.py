import sys
N = int(input())
A = []
for i in range(N) :
    A.append(int(sys.stdin.readline()))
A.sort()
for j in A :
    print(j)