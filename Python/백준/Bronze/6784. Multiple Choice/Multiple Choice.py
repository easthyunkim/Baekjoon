N = int(input())
stu = [input() for _ in range(N)]
ans = [input() for _ in range(N)]
cnt = 0
for i in range(N):
    if stu[i] == ans[i]:
        cnt += 1
print(cnt)