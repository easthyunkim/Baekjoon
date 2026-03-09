t = int(input())
a, b, c, d, e = map(int, input().split())
cnt = 0
for i in [a, b, c, d, e]:
    if i == t:
        cnt += 1
print(cnt)