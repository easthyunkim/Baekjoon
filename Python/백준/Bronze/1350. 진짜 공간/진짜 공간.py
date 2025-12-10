N = int(input())
arr = list(map(int, input().split()))
cluster = int(input())
ans = N

for i in arr:
    if i > cluster:
        ans += (i-1)//cluster
    elif i == 0:
        ans -= 1

print(cluster*ans)