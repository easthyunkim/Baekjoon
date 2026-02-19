import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a, b = input().split()
    a = int(a, 2)
    b = int(b, 2)
    ans = a+b
    print(format(ans, 'b'))