from itertools import combinations
import sys
N, M = map(int, sys.stdin.readline().split())
count = list(map(int, sys.stdin.readline().split()))
my_max = 0
for i in combinations(count, 3):
    my_sum = sum(i)
    if my_max < my_sum <= M :
        my_max = my_sum
print(my_max)