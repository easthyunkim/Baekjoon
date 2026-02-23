import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

if a > 0:
    max_open = a+2*b
else:
    max_open = 2*b

if c > 0:
    max_close = c+2*d
else:
    max_close = 2*d

k = min(max_open, max_close)

if (a == 0 or c == 0) and k%2 != 0:
    k -= 1

if k > 0:
    ans = k*2+e*2+f*2
else:
    ans = e*2

print(ans)