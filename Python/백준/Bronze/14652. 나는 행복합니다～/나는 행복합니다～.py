import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
X = K//M
Y = K%M

print(X, Y)