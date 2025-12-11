N, M = map(int, input().split())
A, B = set(), set()

for i in range(N):
    S = input()
    A.add(S)

for i in range(M):
    S = input()
    B.add(S)

C= sorted(list(A&B))
print(len(C))

for i in range(len(C)):
    print(C[i])