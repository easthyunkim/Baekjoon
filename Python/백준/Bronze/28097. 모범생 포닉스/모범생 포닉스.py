N = int(input())
T = list(map(int, input().split()))
total = sum(T)+(8*(N-1))
d, t = total//24, total%24
print(d, t)