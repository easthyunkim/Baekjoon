n = int(input())
m = int(input())
s = str(input())
i, cnt, ans = 0, 0, 0

while i < (m-1):
    if s[i:i+3] == 'IOI':
        cnt += 1
        i += 2
        if cnt == n:
            ans += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(ans)