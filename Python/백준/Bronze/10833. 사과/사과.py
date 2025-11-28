import sys
input = sys.stdin.readline

N = int(input())
total_apple = 0
for i in range(N):
    student, apple = map(int, input().split())
    apple %= student
    total_apple += apple
print(total_apple)