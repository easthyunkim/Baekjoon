vowel = ['a', 'e', 'i', 'o', 'u']
special = ['ee', 'oo']

while True:
    x = y = 0
    cnt = 0
    word = input()

    if word == 'end':
        break

    for i in vowel:
        if i in word:
            cnt += 1
    if cnt < 1:
        print(f'<{word}> is not acceptable.')
        continue
    
    for i in range(len(word)-2):
        if (word[i] in vowel) and (word[i+1] in vowel) and (word[i+2] in vowel):
            x += 1
        elif not(word[i] in vowel) and not(word[i+1] in vowel) and not(word[i+2] in vowel):
            x += 1
    if x == 1:
        print(f'<{word}> is not acceptable.')
        continue
    
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            if word[i] == 'e' or word[i] == 'o':
                continue
            else:
                y += 1
    if y == 1:
        print(f'<{word}> is not acceptable.')
        continue
    print(f'<{word}> is acceptable.')