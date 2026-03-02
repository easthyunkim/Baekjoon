n = int(input())
for _  in range(n):
    s = input()
    s_lower = s.lower()
    cnt_g, cnt_b = 0, 0
    for i in s_lower:
        if i == 'g':
            cnt_g += 1
        elif i == 'b':
            cnt_b += 1
    if cnt_g == cnt_b:
        print(''.join(s)+' is NEUTRAL')
    elif cnt_g > cnt_b:
        print(''.join(s)+' is GOOD')
    else:
        print(''.join(s)+' is A BADDY')