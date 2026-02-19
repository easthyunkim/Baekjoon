cnt = 0
ans = 0
lst = []
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range(n):
    cnt += arr[i]
    lst.append(cnt)

for i in range(len(lst)):
    ans += lst[i]

print(ans)