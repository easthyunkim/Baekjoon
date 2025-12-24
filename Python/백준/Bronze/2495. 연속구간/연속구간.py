for i in range(3):
    s = str(input())
    now = 1
    cnt = 1
    for i in range(1, 8):
        if s[i-1] == s[i]:
            cnt += 1
        else:
            now = max(now, cnt)
            cnt = 1
    now = max(now, cnt)
    print(now)