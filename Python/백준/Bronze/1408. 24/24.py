import sys
input = sys.stdin.readline

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

ans1 = h1*3600+m1*60+s1
ans2 = h2*3600+m2*60+s2
ans3 = ans2-ans1

if ans3 < 0:
    ans3 += 86400

h3 = ans3//3600
ans3 %= 3600
m3 = ans3//60
ans3 %= 60
s3 = ans3

print("%02d:%02d:%02d" %(h3,m3,s3))