import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}

for i in range(n):
    x = input().strip()
    dict[i+1] = x
    dict[x] = i+1

for j in range(m):
    y = input().strip()
    if y.isdigit():
        print(dict[int(y)])
    else:
        print(dict[y])