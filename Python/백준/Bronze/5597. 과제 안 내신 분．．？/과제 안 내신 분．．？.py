students=[i for i in range(1,31)]
for i in range(28):
    N=int(input())
    students.remove(N)
print(min(students))
print(max(students))