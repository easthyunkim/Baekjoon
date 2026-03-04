lst = []
cnt = 0
for i in range(4):
    a, b = map(int, input().split())
    cnt -= a
    cnt += b
    lst.append(cnt)

print(max(lst))