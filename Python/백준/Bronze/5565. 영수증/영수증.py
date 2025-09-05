import sys
input = sys.stdin.readline

A = int(input())
for i in range(9):
    A -= int(input())
print(A)