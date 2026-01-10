N, M = map(int, input().split())
arr = [input() for _ in range(N)]
ans = -1
for i in range(M):
    tmp = True
    for j in range(N):
        if arr[j][i] == 'O':
            tmp = False
    if tmp:
        ans = i+1
        break
if ans != -1:
    print(ans)
else:
    print('ESCAPE FAILED')