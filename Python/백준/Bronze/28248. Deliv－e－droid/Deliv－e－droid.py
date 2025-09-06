import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
Bonus = 0

if A > B:
    Bonus += 500
else :
    Bonus += 0

print((A*50)-(B*10)+Bonus)