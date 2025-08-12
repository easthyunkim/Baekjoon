import sys
input = sys.stdin.readline
N = int(input())
for _ in range (1, N+1) :
    A, B, C = map(int, input().split())
    print(A*(C-1)+B)