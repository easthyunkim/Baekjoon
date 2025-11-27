import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
eat = A // 2 + B

if N < eat:
    print(N)
else:
    print(eat)