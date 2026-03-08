import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    cnt= 0
    for j in range(10):
        if arr[j] == (j%5)+1:
            cnt += 1
        if cnt == 10:
            print(i+1)