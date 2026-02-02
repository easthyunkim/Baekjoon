n = int(input())
w = int(input())
ans = n*10

if n >= 3:
    ans += 20

if n == 5:
        ans += 50

if w > 1000:
    ans -= 15

if ans > 0:
    print(ans)
else:
    print(0)