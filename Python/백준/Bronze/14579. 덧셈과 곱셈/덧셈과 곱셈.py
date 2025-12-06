import sys
input = sys.stdin.readline

a, b = map(int, input().split())
ans = 1
for i in range(b+1):
    if i < a:
        continue
    ans = (ans*(i*(i+1)//2))%14579
print(ans)