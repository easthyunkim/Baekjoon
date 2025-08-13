import sys
input = sys.stdin.readline
A = int(input())
W, V = map(int, input().split())
B = W/V
if A <= B :
    print(1)
else :
    print(0)