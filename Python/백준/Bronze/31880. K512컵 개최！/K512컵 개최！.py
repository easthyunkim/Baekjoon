import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = sum(A)

for i in B:
    if i == 0:
        continue
    result *= i

print(result)