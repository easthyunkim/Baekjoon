import sys
N = int(sys.stdin.readline())
A = [sys.stdin.readline().strip() for i in range(N)]
A=list(set(A))
A.sort()
A.sort(key=len)
for i in A :
    print(i)