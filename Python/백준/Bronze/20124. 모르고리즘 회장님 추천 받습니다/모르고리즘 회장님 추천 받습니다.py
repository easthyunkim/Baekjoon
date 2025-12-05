N = int(input())
lst = []

for i in range(N):
    A, B = input().split()
    lst.append((A, int(B)))

lst.sort(key=lambda x:(-x[1],x[0]))
print(lst[0][0])