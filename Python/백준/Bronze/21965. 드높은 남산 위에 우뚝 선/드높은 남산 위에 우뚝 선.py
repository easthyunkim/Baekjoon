n = int(input())
arr = list(map(int, input().split()))
mountain = True
updown = True

for i in range(n-1):
    if arr[i] < arr[i+1]:
        if updown == False:
            mountain = False
            break
    elif arr[i] == arr[i+1]:
        mountain = False
        break
    else:
        updown = False

if mountain:
    print('YES')
else:
    print('NO')