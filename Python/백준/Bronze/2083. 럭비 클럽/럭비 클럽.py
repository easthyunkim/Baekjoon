while True:
    N, O, W = input().split()
    if N == '#':
        break
    if int(O) > 17 or int(W) >= 80:
        print(f'{N} Senior')
    else:
        print(f'{N} Junior')