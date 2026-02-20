import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
lst = []

def go(arr):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    for i in range(arr, n+1):
        if i not in lst:
            lst.append(i)
            go(i+1)
            lst.pop()

go(1)