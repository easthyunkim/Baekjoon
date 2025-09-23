#입력 받기
ipt = lambda : map(int, input().split())
N, M = ipt()
A = []
for _ in range(N):
    A.append(list(ipt()))

M, K = ipt()
B = []
for _ in range(M):
    B.append(list(ipt()))


#행렬 곱셈
C = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]

#출력문
for i in C:
    for j in i:
        print(j, end = ' ')
    print()