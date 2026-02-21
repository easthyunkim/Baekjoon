a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())
pi = 3.14159265358979
if p1/a1 > p2/(r1**2*pi):
    print('Whole pizza')
else:
    print('Slice of pizza')