t = int(input())
ans = 0
for i in range(t):
    ans += sum(list(map(int, input().split())))
print(ans)