N, D = map(int, input().split())
for i in range(N):
    ans = ""
    word = input()
    if D == 1:
        for j in word:
            if j == 'd':
                ans += 'q'
            elif j == 'b':
                ans += 'p'
            elif j == 'q':
                ans += 'd'
            elif j == 'p':
                ans += 'b'
    if D == 2:
        for j in word:
            if j == 'd':
                ans += 'b'
            if j == 'b':
                ans += 'd'
            if j == 'q':
                ans += 'p'
            if j == 'p':
                ans += 'q'
    print(ans)