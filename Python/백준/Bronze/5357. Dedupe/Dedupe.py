import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()
    ans = s[0]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            ans += s[i]
    print(ans)