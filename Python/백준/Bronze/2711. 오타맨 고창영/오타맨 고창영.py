T = int(input())
for i in range(T):
    arr = input().split()
    idx, D = int(arr[0]), arr[1]
    print(D[:idx-1]+D[idx:])