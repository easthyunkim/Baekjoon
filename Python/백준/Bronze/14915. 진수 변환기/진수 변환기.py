m, n = map(int, input().split())
def convert(m, n):
    c = '0123456789ABCDEF'
    if m < n:
        return str(c[m])
    else:
        return convert(m//n, n)+str(c[m%n])
print(convert(m, n))