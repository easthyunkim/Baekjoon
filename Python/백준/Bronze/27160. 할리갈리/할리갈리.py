import sys
input = sys.stdin.readline
n = int(input())
fruits = {'STRAWBERRY':0, 'BANANA':0, 'LIME':0, 'PLUM':0}
for i in range(n):
    s, x = input().split()
    fruits[s] += int(x)

if 5 in fruits.values():
    print('YES')
else:
    print('NO')