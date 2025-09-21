import sys
input = sys.stdin.readline

# 입력 받기
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

#조건문으로 경우의 수 분기하기
if A%C == 0:
    A_ans = A//C
else:
    A_ans = (A//C)+1

if B%D == 0:
    B_ans = B//D
else:
    B_ans = (B//D)+1

#출력하기
print(L-max(A_ans, B_ans))