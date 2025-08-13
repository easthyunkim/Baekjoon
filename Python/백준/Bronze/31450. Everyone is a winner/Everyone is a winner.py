import sys
input = sys.stdin.readline
A, B = map(int, input().split())
if A%B == 0 :
    print('Yes')
else :
    print('No')