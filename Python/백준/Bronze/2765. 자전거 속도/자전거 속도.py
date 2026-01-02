i = 1
while 1:
    d, r, s = map(float, input().split())
    pi = 3.1415927
    if r == 0:
        break
    dis = d/63360*pi*r
    mph = dis/s*3600
    print(f'Trip #{i}: {dis:.2f} {mph:.2f}')
    i += 1