T = int(input())
for i in range(T):
    n = int(input())
    a = n//5
    b = n%5
    for i in range(a):
        print('++++', end = ' ')
    for i in range(b):
        print('|', end = '')
    print('')