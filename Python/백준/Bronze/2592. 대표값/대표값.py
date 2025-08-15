import sys
input = sys.stdin.readline
ans = []
for i in range(10):
    N = int(input())
    ans.append(N)

print(sum(ans)//10)
print(max(ans, key=ans.count))
