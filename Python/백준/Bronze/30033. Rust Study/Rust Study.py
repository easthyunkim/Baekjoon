cnt = 0
n = int(input())
a = list(input().split())
b = list(input().split())
for i in range(n):
    if int(a[i]) <= int(b[i]):
        cnt += 1
print(cnt)