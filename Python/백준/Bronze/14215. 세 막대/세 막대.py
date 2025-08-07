import sys
N = list(map(int, sys.stdin.readline().split()))
N.sort()
a, b, c = N
if a+b<=c :
    c=a+b-1
print(a+b+c)