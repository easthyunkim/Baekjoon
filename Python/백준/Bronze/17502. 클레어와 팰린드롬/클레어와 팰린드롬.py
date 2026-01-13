N = int(input())

a = list(input())

if len(a)%2 == 1:
    T = int((len(a)-1)/2)
    if a[T] == '?':
        a[T] = 'a'

for i in range(N//2):
    if a[i] == '?':
        if a[-1-i] != '?':
            a[i] = a[-1-i]
        else:
            a[i] = 'a'
            a[-1-i] = 'a'
    else:
        a[-1-i] = a[i]

print(''.join(a))