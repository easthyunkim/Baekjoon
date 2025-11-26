import sys
input = sys.stdin.readline

N = int(input())
a_score = b_score = 100

for i in range(N):
    a, b= map(int, input().split())
    if a < b:
        a_score -= b
    elif a > b:
        b_score -= a

print(a_score)
print(b_score)