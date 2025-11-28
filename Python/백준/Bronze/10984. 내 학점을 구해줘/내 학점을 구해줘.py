import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    total_grade = 0
    total_gpa = 0
    for j in range(N):
        C, G = map(float, input().split())
        total_grade += C
        total_gpa += C*G
    GPA = total_gpa / total_grade
    print(int(total_grade), '%.1f'%GPA)