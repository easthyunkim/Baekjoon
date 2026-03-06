h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
ans1 = h1*3600+m1*60+s1
ans2 = h2*3600+m2*60+s2

if ans2 > ans1:
    ans = ans2-ans1
else:
    ans = ans2-ans1+24*3600

h = ans//60//60
m = ans//60%60
s = ans%60

print(f'{h:02d}:{m:02d}:{s:02d}')