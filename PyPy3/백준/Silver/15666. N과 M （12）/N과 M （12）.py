import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = sorted(list(set(map(int, input().split()))))
lst = []

def go(k):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(k, len(arr)):
        lst.append(arr[i])
        go(i)
        lst.pop()

go(0)