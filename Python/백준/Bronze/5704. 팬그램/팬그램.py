while True:
    S = input()
    if S == '*':
        break
    D = {}
    for i in range(26):
        D[chr(97+i)] = 0

    for i in range(len(S)):
        if 97 <= ord(S[i]) <= 122:
            D[S[i]] += 1
    
    temp = True
    key = list(D.keys())
    for i in range(len(key)):
        if D[key[i]] == 0:
            temp = False
    if temp == True:
        print('Y')
    else:
        print('N')