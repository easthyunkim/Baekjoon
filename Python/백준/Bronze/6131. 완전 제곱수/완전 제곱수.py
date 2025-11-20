import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(1, 500):
    A = (i**2+N)**0.5
    if A % 1 == 0:
        cnt += 1

print(cnt)