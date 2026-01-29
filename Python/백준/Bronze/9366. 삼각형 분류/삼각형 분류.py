n = int(input())
for i in range(n):
    a = sorted(list(map(int, input().split())))
    print(f'Case #{i+1}: ', end='')
    if a[0]+a[1] <= a[2]:
        print("invalid!")
    elif a[0] == a[1] == a[2]:
        print("equilateral")
    elif a[0]==a[1] or a[1]==a[2] or a[2]==a[0]:
        print("isosceles")
    else:
        print("scalene")