n = int(input())
a = int(input())

if n <= 5:
    for i in range(n-1):
        if a == 1:
            print(0)
            a = 0
        else:
            print(1)
            a = 1
else:
    print('Love is open door')