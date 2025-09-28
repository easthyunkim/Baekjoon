import sys
input = sys.stdin.readline

#입력받기
R, C, N = map(int, input().split())
row = R//N
column = C//N

#필요한 CCTV 수 계산하기
if R%N!=0:
    row += 1
if C%N!=0:
    column += 1

#출력하기
print(row*column)