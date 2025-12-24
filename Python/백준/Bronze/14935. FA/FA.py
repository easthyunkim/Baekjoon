x = input()
while True:
    fx = int(x[0])*len(x)
    if int(x) == fx:
        print('FA')
        break
    x = str(fx)
else:
    print('NFA')