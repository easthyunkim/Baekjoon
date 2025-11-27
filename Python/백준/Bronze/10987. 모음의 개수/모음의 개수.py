N = list(input())
ans = 0

for i in N:
    if i in ['a', 'e', 'i', 'o', 'u']:
        ans += 1

print(ans)