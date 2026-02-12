a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
def f_n(n):
    f_n = a1*n+a0
    return f_n
if f_n(n0) <= c*n0 and a1 <= c:
    print(1)
else:
    print(0)