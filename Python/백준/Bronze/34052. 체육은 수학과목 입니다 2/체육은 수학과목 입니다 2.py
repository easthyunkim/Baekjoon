import sys
input = sys.stdin.readline
T = [int(input()) for _ in range(4)]
LT = 1800 - sum(T)
if LT >= 300 :
    print('Yes')
else :
    print('No')