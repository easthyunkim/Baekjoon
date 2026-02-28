import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

def selection_sort(n):
    cnt = 0
    for i in range(n-1, 0, -1):
        last = i
        for j in range(i-1, -1, -1):
            if lst[j] > lst[last]:
                last = j
        if last != i:
            lst[i], lst[last] = lst[last], lst[i]
            cnt += 1
        if cnt == k:
            return print(lst[last], lst[i])
    return print(-1)

selection_sort(n)