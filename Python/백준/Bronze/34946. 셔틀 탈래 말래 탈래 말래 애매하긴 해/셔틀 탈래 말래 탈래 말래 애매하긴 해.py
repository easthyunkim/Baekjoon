A, B, C, D = map(int, input().split())
ans1 = D-(A+B)
ans2 = D-C
if ans1 >= 0 and ans2 >= 0:
    print('~.~')
elif ans1 >= 0 and ans2 < 0:
    print('Shuttle')
elif ans1 < 0 and ans2 >= 0:
    print('Walk')
else:
    print('T.T')