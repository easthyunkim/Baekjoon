word = ['A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z']
T = int(input())
for i in range(T):
    S = input()
    ans = 0
    for i in word:
        if i not in S:
            ans += ord(i)
    print(ans)