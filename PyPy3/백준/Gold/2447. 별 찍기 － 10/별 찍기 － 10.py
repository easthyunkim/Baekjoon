init = ['***', '* *', '***']
N = int(input())

def star(n = 3, arr = init):
    lst = []
    if n == N:
        return arr
    for i in range(n):
        lst.append(arr[i]*3)
    for i in range(n):
        lst.append(arr[i]+' '*n+arr[i])
    for i in range(n):
        lst.append(arr[i]*3)
    return star(n*3, lst)

ans = star(3, init)

for i in ans:
    print(i)