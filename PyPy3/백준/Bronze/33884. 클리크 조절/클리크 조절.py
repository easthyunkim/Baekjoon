import sys
input = sys.stdin.readline
n = int(input())
arr_1 = [list(map(int, input().split())) for _ in range(n)]
arr_2 = [list(map(int, input().split())) for _ in range(n)]
arr_1.sort()
arr_2.sort()
a = arr_2[0][0]-arr_1[0][0]
b = arr_2[0][1]-arr_1[0][1]
print(a, b)