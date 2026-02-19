n, k = map(int, input().split())
arr = []
ans = 0

for i in range(n):
    a = int(input())
    arr.append(a)

for i in range(n):
    temp = arr.pop()
    ans += k//temp
    k %= temp

print(ans)