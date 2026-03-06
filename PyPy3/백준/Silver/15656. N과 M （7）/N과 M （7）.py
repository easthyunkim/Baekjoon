import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = sorted(list(map(int, input().split())))
lst = []

def go():
    if len(lst) == m:
        print(*lst)
        return

    for i in range(n):
        lst.append(arr[i])
        go()
        lst.pop()

go()