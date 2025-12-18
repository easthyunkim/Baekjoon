T = int(input())
for i in range(T):
    A, B = list(map(str, input().split()))
    A_sort = sorted(A)
    B_sort = sorted(B)
    if A_sort == B_sort:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')