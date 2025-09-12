import sys
input = sys.stdin.readline
for _ in range(int(input())):
    P, T = map(int, input().split())
    print(P+(T//4)-(T//7))