N, M = map(int, input().split())
j = int(input())
apples = []
now = 1
ans = 0

for i in range(j):
    a = int(input())
    apples.append(a)

for i in apples:
    if now <= i and now+(M-1) >= i:
        pass
    elif now > i:
        ans += abs(i-now)
        now = i
    else:
        ans += i-(M-1)-now
        now = i-(M-1)

print(ans)