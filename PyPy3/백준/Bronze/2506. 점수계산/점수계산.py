n = int(input())
arr = list(map(int, input().split()))
cnt = 0
ans = 0

for i in range(n):
    if arr[i] == 1:
        cnt += 1
        ans += cnt
    else:
        cnt = 0

print(ans)