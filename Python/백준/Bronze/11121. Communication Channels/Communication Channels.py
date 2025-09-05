import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    A, B = input().split()
    if A == B:
        print('OK')
    else:
        print('ERROR')