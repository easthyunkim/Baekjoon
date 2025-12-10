N, W, H, L = map(int, input().split())
A = W//L
B = H//L
if N > A*B:
    print(A*B)
else:
    print(N)