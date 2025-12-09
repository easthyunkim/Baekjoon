while True:
    S = input()

    ans = 0

    if S == '#':
        break

    for i in range(len(S)):
        if S[i] == 'a' or S[i] == 'e' or S[i] == 'i' or S[i] == 'o' or S[i] == 'u':
            ans += 1
        if S[i] == 'A' or S[i] == 'E' or S[i] == 'I' or S[i] == 'O' or S[i] == 'U':
            ans += 1
    
    print(ans)