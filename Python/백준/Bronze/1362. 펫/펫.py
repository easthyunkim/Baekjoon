cnt = 0
while True:
    cnt += 1
    death = 0
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break
    while True:
        s1, s2 = input().split()
        s2 = int(s2)
        if s1 == '#' and s2 == 0:
            break
        if s1 == 'E':
            w -= s2
        else:
            w += s2
        if w <= 0:
            death = 1
    
    if death == 1:
        print(f'{cnt} RIP')
    else:
        if w > o/2 and w < o*2:
            print(f'{cnt} :-)')
        else:
            print(f'{cnt} :-(')