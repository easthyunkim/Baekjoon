n = int(input())
arr = [[], [], []]
ans = []

for _ in range(n):
    a, b, c = map(int, input().split())
    arr[0].append(a)
    arr[1].append(b)
    arr[2].append(c)

for i in range(n):
    cnt = 0
    for j in range(3):
        if arr[j].count(arr[j][i]) == 1:
            cnt += arr[j][i]
        else:
            cnt += 0
    ans.append(cnt)

for i in ans:
    print(i)