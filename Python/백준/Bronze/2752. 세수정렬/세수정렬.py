import sys
input = sys.stdin.readline
N = list(map(int, input().split()))
N.sort()
print(N[0], N[1], N[2])