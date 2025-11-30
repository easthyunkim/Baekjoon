import sys
input = sys.stdin.readline

x, y, p, a, b = map(int, input().split())

ans1 = p+b*(y-1)

ans2 = x*ans1-a*(x*(x-1)//2)

print(ans2)