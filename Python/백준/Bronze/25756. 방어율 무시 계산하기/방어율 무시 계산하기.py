N = int(input())
A = map(int, input().split())
V = 0

for i in A:
    X = 1 - (V / 100)
    Y = 1 - (i / 100)
    V = (1 - (X * Y)) * 100
    print(V)