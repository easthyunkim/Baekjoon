import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
for i in range(N):
    A, B = map(int, input().split())
    cnt += A
    cnt -= B
    print(cnt)