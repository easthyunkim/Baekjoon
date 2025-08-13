import sys
input = sys.stdin.readline
N = int(input())
A = [1 for _ in range(N) if int(input()) % 2 == 1]
print(len(A))