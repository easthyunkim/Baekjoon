S = input()
words= 'SciComLove'
ans = 0

for i in range(len(S)):
    if words[i] != S[i]:
        ans += 1

print(ans)