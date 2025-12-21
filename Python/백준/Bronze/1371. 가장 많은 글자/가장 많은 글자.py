word = [0 for i in range(26)]
while True:
    try:
        A = str(input())
        for j in A:
            if j.islower():
                word[ord(j)-97] += 1
    except EOFError:
        break
for i in range(26):
    if word[i] == max(word):
        print(chr(i+97), end='')