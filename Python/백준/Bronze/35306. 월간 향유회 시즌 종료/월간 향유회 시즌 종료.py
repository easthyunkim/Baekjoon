n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_col = [0]*k
cnt = [0]*k
ans = 0

for j in range(k):
    max_col_2 = 0
    cnt_2 = 0
    for i in range(n):
        if arr[i][j] > max_col_2:
            max_col_2 = arr[i][j]
            cnt_2 = 1
        elif arr[i][j] == max_col_2:
            cnt_2 += 1
        max_col[j] = max_col_2
        cnt[j] = cnt_2

for i in range(n):
    for j in range(k):
        if arr[i][j] == max_col[j] and cnt[j] == 1:
            ans += 1
            break

print(ans)