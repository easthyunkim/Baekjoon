import sys
input = sys.stdin.readline

n = int(input())
d = {}

for i in range(n):
    card = int(input())
    if card in d:
        d[card] += 1
    else:
        d[card] = 1

ans = sorted(d.items(), key=lambda x:(-x[1], x[0]))
print(ans[0][0])