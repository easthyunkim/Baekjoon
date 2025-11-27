num = 1

while True:
    N = input()
    if N == '0':
        break
    else:
        r, w, l = map(int, N.split())
    
    table = r*2
    pizza = (w**2+l**2)**0.5
    
    if table >= pizza:
        print(f'Pizza {num} fits on the table.')
    else:
        print(f'Pizza {num} does not fit on the table.')
    
    num += 1