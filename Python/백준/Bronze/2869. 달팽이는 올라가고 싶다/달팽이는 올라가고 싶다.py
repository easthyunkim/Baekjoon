import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())
ans = (V-B)/(A-B)
if ans == int(ans):
    print(int(ans))
else:
    print(int(ans)+1)