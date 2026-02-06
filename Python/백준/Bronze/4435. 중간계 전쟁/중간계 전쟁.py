t = int(input())
for i in range(t):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr1_ans = arr1[0]+arr1[1]*2+arr1[2]*3+arr1[3]*3+arr1[4]*4+arr1[5]*10
    arr2_ans = arr2[0]+arr2[1]*2+arr2[2]*2+arr2[3]*2+arr2[4]*3+arr2[5]*5+arr2[6]*10
    if arr1_ans < arr2_ans:
        print(f'Battle {i+1}: Evil eradicates all trace of Good')
    elif arr1_ans > arr2_ans:
        print(f'Battle {i+1}: Good triumphs over Evil')
    else:
        print(f'Battle {i+1}: No victor on this battle field')