n, k = map(int, input().split())
cnt = []
for i in range(k):
    cnt.append(int(str(n*(i+1))[::-1]))
print(max(cnt))