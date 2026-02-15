import sys
input = sys.stdin.readline

T = int(input())
N = 40
cnt0 = [0]*(N+1)
cnt1 = [0]*(N+1)
cnt0[0], cnt0[1] = 1, 0
cnt1[0], cnt1[1] = 0, 1

for i in range(2, N+1):
    cnt0[i] = cnt0[i-1]+cnt0[i-2]
    cnt1[i] = cnt1[i-1]+cnt1[i-2]

for i in range(T):
    n = int(input())
    print(cnt0[n], cnt1[n])