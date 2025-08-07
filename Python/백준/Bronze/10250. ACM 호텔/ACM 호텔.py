import sys
T = int(sys.stdin.readline())
for i in range(T) :
    H, W, N = map(int, sys.stdin.readline().split())
    A = N % H
    B = N // H + 1
    if A == 0:
        B -= 1
        A = H
    print(A*100 + B)