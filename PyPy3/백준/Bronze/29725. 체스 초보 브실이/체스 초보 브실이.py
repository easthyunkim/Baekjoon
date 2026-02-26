pts = {'K':0,
       'k':0,
       'P':1,
       'p':1,
       'N':3,
       'n':3,
       'B':3,
       'b':3,
       'R':5,
       'r':5,
       'Q':9,
       'q':9}

white, black = 0, 0

for _ in range(8):
    arr = input()
    for i in arr:
        if i == '.':
            continue
        if i.isupper():
            white += pts[i]
        else:
            black += pts[i]

print(white-black)