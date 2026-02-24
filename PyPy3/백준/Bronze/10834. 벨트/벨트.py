m = int(input())
d = 0
n = 1

for i in range(m):
    arr = list(map(int, input().split()))
    d = (d+arr[2])%2
    n = int(n*arr[1]/arr[0])

print(d, n)