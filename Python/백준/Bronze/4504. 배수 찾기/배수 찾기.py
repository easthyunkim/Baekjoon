N = int(input())
while 1:
    num = int(input())
    if num == 0:
        break
    if num % N == 0:
        print(f'{num} is a multiple of {N}.')
    else:
        print(f'{num} is NOT a multiple of {N}.')