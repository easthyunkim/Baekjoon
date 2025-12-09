N = int(input())
s = input()
cnt_2 = 0
cnt_e = 0

for i in range(N):
    if s[i] == '2':
        cnt_2 += 1
    else:
        cnt_e += 1

if cnt_2 > cnt_e:
    print('2')
elif cnt_2 < cnt_e:
    print('e')
else:
    print('yee')