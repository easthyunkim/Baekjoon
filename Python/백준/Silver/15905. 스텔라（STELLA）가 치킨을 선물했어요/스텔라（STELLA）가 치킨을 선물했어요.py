import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

arr_sorted = sorted(arr, key=lambda x:(x[0], -x[1]), reverse=True)

for i in range(n):
    if arr_sorted[4][0] == arr_sorted[i][0] and arr_sorted[4][1] < arr_sorted[i][1]:
        cnt += 1

print(cnt)