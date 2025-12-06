T = int(input())

for i in range(T):
    N = int(input())
    s1, s2 = 0, 0
    for i in range(N):
        p1, p2 = input().split()
        if p1 == p2:
            continue
        else:
            if p1 == 'R' and p2 == 'S' :
                s1 += 1
            elif p1 == 'R' and p2 == 'P' :
                s2 += 1
            elif p1 == 'P' and p2 == 'R' :
                s1 += 1
            elif p1 == 'P' and p2 == 'S' :
                s2 += 1
            elif p1 == 'S' and p2 == 'P' :
                s1 += 1
            elif p1 == 'S' and p2 == 'R' :
                s2 += 1
    if s1 > s2:
        print('Player 1')
    elif s1 < s2:
        print('Player 2')
    else:
        print('TIE')