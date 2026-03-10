n = int(input())
lst = []

one, two, flag = 0, 0, 0
for i in range(n):
    team, time = input().split()
    m, s = map(int, time.split(':'))

    if team == '1':
        if flag == 0:
            one += 48*60-(60*m+s)
        flag += 1
        if flag == 0:
            if two > 0:
                two = two-(48*60-(60*m+s))
    
    else:
        if flag == 0:
            two += 48*60-(60*m+s)
        flag -= 1
        if flag == 0:
            if one >0:
                one = one-(48*60-(60*m+s))

print(f'{one//60:02d}:{one%60:02d}')
print(f'{two//60:02d}:{two%60:02d}')