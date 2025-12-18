N = int(input())
S = list(input())
lst = []
for i in S:
    lst.append(ord(i)-64)
print(sum(lst))