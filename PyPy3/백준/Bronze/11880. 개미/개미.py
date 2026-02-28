import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    d1 = (a**2)+((b+c)**2)
    d2 = (b**2)+((c+a)**2)
    d3 = (c**2)+((a+b)**2)
    print(min(d1, d2, d3))