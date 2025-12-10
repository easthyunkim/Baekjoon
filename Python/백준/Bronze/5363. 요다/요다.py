N = int(input())
for i in range(N):
    arr = list(input().split())
    print(' '.join(arr[2:]+arr[:2]))