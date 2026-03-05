t = int(input())
lst = []
for _ in range(t):
    arr = list(map(int, input().split()))
    lst = []
    for i in arr:
        if i%2 == 0:
            lst.append(i)
    print(sum(lst), min(lst))