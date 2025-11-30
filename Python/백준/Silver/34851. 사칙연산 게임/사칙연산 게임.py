import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
A = (10**9)+7
ans = lst[0]%A
ans2 = lst[0] == 1

for i in lst[1:]:
    if ans2 or i == 1:
        ans = (ans+i)%A
        ans2 = False
    else:
        ans = (ans*i)%A
        ans2 = False

print(ans)