n = int(input())
s = list(input().rstrip())
for _ in range(n-1):
    a = input().rstrip()
    for i in range(len(s)):
        if s[i] != a[i]:
            s[i] = '?'

print(''.join(s))