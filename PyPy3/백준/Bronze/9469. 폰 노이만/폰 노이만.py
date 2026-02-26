import sys
input = sys.stdin.readline

p = int(input())
for i in range(p):
    n, d, a, b, f = map(float, input().split())
    t = d/(a+b)*f
    print('%d %.6f'%(n, t))