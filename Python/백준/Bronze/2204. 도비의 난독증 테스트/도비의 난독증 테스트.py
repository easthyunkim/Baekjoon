while 1:
    n = int(input())
    if n == 0:
        break
    word = []
    for i in range(n):
        word.append(input())
    word.sort(key=str.lower)
    print(word[0])