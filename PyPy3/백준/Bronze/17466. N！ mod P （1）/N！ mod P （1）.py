import sys
input = sys.stdin.readline

N, P = map(int, input().split())
cnt = 1

for i in range(2, N+1):
    cnt = (cnt*i)%P
print(cnt%P)