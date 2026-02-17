import sys
input = sys.stdin.readline

n, k_1 = map(int, input().split())
arr = []


for i in range(n):
    k_2, g, s, b = map(int, input().split())
    arr.append([k_2, g, s, b])

arr_sorted = sorted(arr, key=lambda x:(x[0], x[1], x[2], x[3]))

for i in range(n):
    if arr_sorted[i][0] == k_1:
        ranking = i

for i in range(n):
    if arr_sorted[ranking][1:] == arr_sorted[i][1:]:
        print(i+1)
        break