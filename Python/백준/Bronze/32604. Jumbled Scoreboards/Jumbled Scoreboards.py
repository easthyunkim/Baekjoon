import sys
input = sys.stdin.readline

n = int(input().strip())
prev_a, prev_b = -1, -1
ans = True

for _ in range(n):
    a, b = map(int, input().split())
    if a < prev_a or b < prev_b:
        ans = False
    prev_a, prev_b = a, b

print("yes" if ans else "no")