n = int(input())
for i in range(n):
    s = sorted(list(map(int, input().split())))
    print(f'Scenario #{i+1}:')
    if s[0]**2+s[1]**2 == s[2]**2:
        print('yes\n')
    else:
        print('no\n')