def ans1(x, y):
    if (0 <= x <= 23) and (0 <= y <= 59):
        ans1 = 'Yes'
    else:
        ans1 = 'No'
    return ans1

def ans2(x, y):
    month0 = [4, 6, 9, 11]
    month1 = [1, 3, 5, 7, 8, 10, 12]
    month2 = [2]
    if (x in month0) and (1 <= y <= 30):
        ans2 = 'Yes'
    elif (x in month1) and (1 <= y <= 31):
        ans2 = 'Yes'
    elif (x in month2) and (1 <= y <= 29):
        ans2 = 'Yes'
    else:
        ans2 = 'No'
    return ans2

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    print(f'{ans1(x, y)} {ans2(x, y)}')