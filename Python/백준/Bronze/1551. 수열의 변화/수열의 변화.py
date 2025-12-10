N, K = map(int, input().split())
A = list(map(int, input().split(',')))

for i in range(K):
    for j in range(len(A)-1):
        A.append(A[1]-A[0])
        A.pop(0)
    A.pop(0)

print(','.join(map(str, A)))