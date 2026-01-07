N = int(input())
K = input()
h = j = 0
for i in range(len(K)):
    if int(K[i])%2 == 0:
        j += 1
    else:
        h += 1

if j > h:
    print(0)
elif j < h:
    print(1)
else:
    print(-1)