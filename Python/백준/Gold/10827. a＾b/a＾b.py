from decimal import Decimal, getcontext
getcontext().prec = 10000
A, B = map(str, input().split())
print("{0:f}".format(Decimal(A) ** int(B)))