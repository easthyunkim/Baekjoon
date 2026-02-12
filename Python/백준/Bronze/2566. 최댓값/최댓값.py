arr = [list(map(int, input().split())) for _ in range(9)]
ans = 0
row, col = 0, 0
for i in range(9):
    for j in range(9):
        if arr[i][j] >= ans:
            ans = arr[i][j]
            row = i+1
            col = j+1
print(ans)
print(row, col)