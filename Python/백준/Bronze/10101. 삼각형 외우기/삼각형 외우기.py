import sys
input = sys.stdin.readline

# 입력 받기
A = int(input())
B = int(input())
C = int(input())

#조건문으로 경우의 수 분기하고 출력하기
if A==B==C==60:
    print('Equilateral')
elif A+B+C==180 and A==B:
    print('Isosceles')
elif A+B+C==180 and B==C:
    print('Isosceles')
elif A+B+C==180 and A==C:
    print('Isosceles')
elif A+B+C==180 and A!=B!=C:
    print('Scalene')
elif A+B+C!=180:
    print('Error')