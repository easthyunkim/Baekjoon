cnt = 0
ans = []

for i in range(10):
    a, b = map(int, input().split())
    cnt -= a
    cnt += b
    ans.append(cnt)

ans.sort()
print(ans[-1])