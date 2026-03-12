while True:
    key = input().rstrip()
    if key == '0':
        break
    s = input().rstrip()
    ans = []
    for i in range(len(s)):
        if s[i] == ' ':
            ans.append(' ')
            continue
        res = (ord(s[i])+(ord(key[i%len(key)]))+1)%26+65
        ans.append(chr(res))
    print(''.join(ans))