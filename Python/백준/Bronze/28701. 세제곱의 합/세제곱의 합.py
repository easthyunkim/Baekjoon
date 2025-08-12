import sys
input = sys.stdin.readline
N = int(input())
sum = 0
sum_a = 0
for i in range(1, N+1) :
    sum += i
    sum_a += i**3
print(sum)
print(sum**2)
print(sum_a)