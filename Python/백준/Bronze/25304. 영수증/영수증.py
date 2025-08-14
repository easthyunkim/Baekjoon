import sys
input = sys.stdin.readline
X = int(input())
N = int(input())
cnt = 0
for i  in range(N):
    A, B = map(int, input().split())
    cnt += (A*B)
if X == cnt :
    print('Yes')
else :
    print('No')