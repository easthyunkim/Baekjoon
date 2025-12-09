while True:
    s = input()
    if s == 'EOI':
        break
    s = s.lower()

    nemo = False
    for i in range(len(s)):
        if s[i:i+4] == 'nemo':
            nemo = True
            break
    if nemo == True:
        print('Found')
    else:
        print('Missing')