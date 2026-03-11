import math
import sys
input = sys.stdin.readline

n = int(input())
lst, ans = [], []
gcd = 0

for _ in range(n):
    num = int(input())
    lst.append(num)

gcd = abs(lst[1]-lst[0])

for i in range(2, n):
    gcd = math.gcd(abs(lst[i]-lst[i-1]), gcd)

for i in range(2, int(math.sqrt(gcd))+1):
    if gcd%i == 0:
        ans.append(i)
        ans.append(gcd//i)

ans.append(gcd)
ans = list(set(ans))
ans.sort()

for i in ans:
    print(i, end=' ')