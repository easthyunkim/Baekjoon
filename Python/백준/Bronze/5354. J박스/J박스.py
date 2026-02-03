t = int(input())
for _ in range(t):
    j = int(input())
    if j < 3:
        for i in range(j):
            print('#'*j)
        print()
    else:
        print('#'*j)
        for i in range(j-2):
            print('#'+'J'*(j-2)+'#')
        print('#'*j)
        print()