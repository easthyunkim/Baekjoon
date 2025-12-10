while 1:
    s = list(input())
    if s == ['*', '*', '*']:
        break
    print(''.join(s[::-1]))