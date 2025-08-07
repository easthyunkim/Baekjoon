N = []
for i in range(10) :
    A = int(input())
    B= A % 42
    N.append(B)
C=set(N)
print(len(C))