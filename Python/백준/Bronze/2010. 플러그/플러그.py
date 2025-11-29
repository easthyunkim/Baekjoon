import sys
input = sys.stdin.readline

N = int(input())
ans = 0

for i in range(N):
    outlet = int(input())
    ans += outlet

print(ans-(N-1))