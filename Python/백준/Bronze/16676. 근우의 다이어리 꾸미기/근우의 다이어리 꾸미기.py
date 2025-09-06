import sys
input = sys.stdin.readline

N = int(input())
C = 1

if N <= 10:
    print(1)
else:
    while N >= C:
        C = str(C)
        C += '1'
        C = int(C)
    print(len(str(C//10)))