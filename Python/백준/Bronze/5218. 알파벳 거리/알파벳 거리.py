T = int(input())

for i in range(T):
    A, B = input().split()
    ans = []
    for j in range(len(A)):
        x = ord(A[j])-64
        y = ord(B[j])-64
        if y >= x:
            z = y-x
        else:
            z = (y+26)-x
        ans.append(z)
    print(f'Distances: {' '.join(map(str, ans))}')