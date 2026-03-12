n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))
cnt = l
for i in range(n):
    if arr[i] <= cnt:
        cnt += 1
    else:
        break
print(cnt)