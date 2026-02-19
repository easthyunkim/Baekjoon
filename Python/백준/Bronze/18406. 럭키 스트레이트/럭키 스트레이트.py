n = list(map(int, input()))
half = len(n)//2
a = 0
b = 0

for i in range(0, half):
    a += n[i]

for i in range(half, len(n)):
    b += n[i]

if a == b:
    print('LUCKY')
else:
    print('READY')