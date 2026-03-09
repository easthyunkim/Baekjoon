import sys

imput = sys.stdin.readline

y, c, p = map(int, input().split())

print(min(y, c//2, p))