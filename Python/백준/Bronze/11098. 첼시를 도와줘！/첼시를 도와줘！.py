import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    p = int(input())
    list = []
    for _ in range(p):
        cost, name = input().split()
        cost = int(cost)
        list.append((cost, name))
        list.sort()
    print(list[_][1])