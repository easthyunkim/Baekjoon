n, s = map(str, input().split())
if n == '1':
    print(s)
    s1 = s
    i = 0
    while True:
        if s1[i].isupper() == True:
            s1 = s1[:i]+"_"+s1[i].lower()+s1[i+1:]
            i = i+2
        else:
            i = i+1
        if i >= len(s1):
            break
    print(s1)
    print(s[0].upper()+s[1:])

if n == '2':
    s2 = s
    for i in range(len(s2)):
        if s2[i] == '_':
            s2 = s2[:i+1]+s[i+1].upper()+s[i+2:]
    s2 = s2.replace('_','')
    print(s2)
    print(s)
    print(s2[0].upper()+s2[1:])

if n == '3':
    print(s[0].lower()+s[1:])
    s3 = s
    i = 0
    while True:
        if s3[i].isupper() == True:
            s3 = s3[:i]+"_"+s3[i].lower()+s3[i+1:]
            i = i+2
        else:
            i = i+1
        if i >= len(s3):
            break
    print(s3[1:])
    print(s)