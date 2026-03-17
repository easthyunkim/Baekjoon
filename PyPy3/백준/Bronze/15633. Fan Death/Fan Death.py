n = int(input())
lst = []

for i in range(1, n+1):
    if n%i == 0:
        lst.append(i)

print((sum(lst))*5-24)