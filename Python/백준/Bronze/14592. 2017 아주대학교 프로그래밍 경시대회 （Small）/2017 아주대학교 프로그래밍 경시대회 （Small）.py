import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    s, c, l = map(int, input().split())
    arr.append([s, c, l])

arr_sorted = sorted(arr, key=lambda x:(-x[0], x[1], x[2]))

print(arr.index(arr_sorted[0])+1)