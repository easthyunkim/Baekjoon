import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
max1 = A*B/C
max2 = A/B*C
if max1 > max2:
    print(int(max1))
else:
    print(int(max2))