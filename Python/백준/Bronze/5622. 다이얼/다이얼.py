dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
A = input()
ans = 0
for j in range(len(A)):
    for i in dial:
        if A[j] in i:
            ans += dial.index(i) + 3
print(ans)