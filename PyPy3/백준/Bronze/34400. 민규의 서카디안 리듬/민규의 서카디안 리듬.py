T = int(input())
for i in range(T):
    t = int(input())
    if t%25 < 17:
        print('ONLINE')
    else:
        print('OFFLINE')