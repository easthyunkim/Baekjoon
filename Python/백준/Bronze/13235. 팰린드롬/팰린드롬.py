s = input()
flag = True
x, y = 0, len(s)-1
while 1:
    if x >= y:
        break
    if s[x] != s[y]:
        flag = False
    x += 1
    y -= 1
if flag == True:
    print('true')
else:
    print('false')