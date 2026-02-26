import sys
input = sys.stdin.readline

n = int(input())
arr = [[0]*100 for _ in range(100)]
ans = 0

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1

for i in range(100):
    ans += arr[i].count(1)

print(ans)