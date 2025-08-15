import sys
input = sys.stdin.readline
ans = []
for i in range(5):
    N = int(input())
    ans.append(N)

ans.sort()
print(sum(ans)//5)
print(ans[2])
