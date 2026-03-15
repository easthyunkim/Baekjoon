import sys
input = sys.stdin.readline

n = int(input())
arr = [0, 1, 2]
lst = []
tmp = []
visited = [True]*n

def go(a):
    if len(a) == n:
        k = 0
        for i in range(n):
            k += a[i]*(10**(n-i-1))
        tmp.append(k)
        return
    for i in arr:
        a.append(i)
        go(a)
        a.pop()
go(lst)
ans = 0
for k in tmp:
    if k%3 == 0 and len(str(k)) == n:
        if k != 0:
            ans += 1
print(ans)