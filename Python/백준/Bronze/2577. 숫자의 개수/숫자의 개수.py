A, B, C = map(int,open(0).read().split())
D = list(str(A*B*C))
for i in range (10) :
    print(D.count(str(i)))