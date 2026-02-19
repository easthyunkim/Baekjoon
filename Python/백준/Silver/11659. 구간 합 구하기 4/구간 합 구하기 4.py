import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
lst = [0]
ans = 0

for i in range(n):
    ans += arr[i]
    lst.append(ans)

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    print(lst[b]-lst[a])