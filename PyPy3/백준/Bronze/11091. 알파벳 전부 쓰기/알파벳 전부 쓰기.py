n = int(input())
alpha = set('abcdefghijklmnopqrstuvwxyz')
for _ in range(n):
    s = set(input().lower())
    ans = sorted(list(alpha-s))
    if ans:
        print('missing', ''.join(ans))
    else:
        print('pangram')