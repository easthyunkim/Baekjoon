
N = int(input())
S = list('Simon says')
for i in range(N):
    arr = list(input())
    if arr[:10] == S:
        print(''.join(arr[10:]))