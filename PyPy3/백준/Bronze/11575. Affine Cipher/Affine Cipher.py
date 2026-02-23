t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    s = list(input())
    for i in range(len(s)):
        ans = (a*(ord(s[i])-ord('A'))+b)%26
        s[i] = chr(ans+ord('A'))
    print(''.join(s))