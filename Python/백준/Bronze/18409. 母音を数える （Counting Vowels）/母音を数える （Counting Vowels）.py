N = int(input())
S = input()
T = 0
for _ in S :
    if _ in ['a', 'i', 'u', 'e', 'o'] :
        T += 1
print(T)