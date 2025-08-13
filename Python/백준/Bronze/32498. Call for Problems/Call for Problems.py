import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
for _ in range(N):
    P = int(input())
    if P % 2 == 1:
        cnt += 1
print(cnt)