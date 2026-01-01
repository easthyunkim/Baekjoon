n, b = map(int, input().split())

D = {}
ans = []

for i in range(10):
    D[i] = str(i)
for i in range(26):
    D[i+10] = chr(65+i)

while 1:
    if n == 0:
        break
    x = n%b
    ans.append(D[x])
    n //= b

print(''.join(ans[::-1]))