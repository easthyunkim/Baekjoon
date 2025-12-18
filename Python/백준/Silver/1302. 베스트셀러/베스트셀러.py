N = int(input())
D = {}
for i in range(N):
    S = input()
    if S in D:
        D[S] += 1
    else:
        D[S] = 1

arr = list(D.items())
arr.sort(key=lambda x:(-x[1], x[0]))
print(arr[0][0])