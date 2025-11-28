import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    name, d, m, y = input().split()
    d, m, y =map(int, (d, m, y))
    lst.append((y, m, d, name))
    lst.sort()

print(lst[-1][3])
print(lst[0][3])