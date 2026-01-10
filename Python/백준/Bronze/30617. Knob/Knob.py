import sys
input = sys.stdin.readline
T = int(input())
cnt = 0
x = y = 0
for i in range(T):
    l, r = map(int, input().split())
    if i > 0:
        if x == l and x != 0:
            cnt += 1
        if y == r and y != 0:
            cnt += 1
    if l == r and l != 0:
        cnt += 1
    x, y = l, r
print(cnt)