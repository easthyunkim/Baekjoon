N = int(input())
company = {}
for i in range(N): 
    x, y = input().split()
    company[x] = y

key = list(company.keys())
ans = []
for i in range(len(key)):
    if company[key[i]] == 'enter':
        ans.append(key[i])

ans = sorted(ans, reverse=True)
for i in range(len(ans)):
    print(ans[i])