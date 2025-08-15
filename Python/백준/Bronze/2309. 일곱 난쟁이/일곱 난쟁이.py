import sys
input = sys.stdin.readline
ans = []
for i in range(9):
    N = int(input())
    ans.append(N)

ans.sort()
w1, w2 = 0, 0

for i in range(9):
    for j in range(9):
        if sum(ans)-ans[i]-ans[j] == 100 and i!=j:
            w1, w2 = i, j

for i in range(9) :
    if i != w1 and i != w2:
        print(ans[i])