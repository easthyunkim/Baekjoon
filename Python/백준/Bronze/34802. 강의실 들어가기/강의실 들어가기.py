h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t, k = map(int, input().split())
time1 = 3600*h1+60*m1+s1
time2 = 3600*h2+60*m2+s2
ans = t*(100-k)/100
if ans <= time2-time1:
    print(1)
else:
    print(0)