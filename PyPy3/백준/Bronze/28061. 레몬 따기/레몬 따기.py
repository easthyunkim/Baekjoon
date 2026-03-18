n = int(input())
arr = list(map(int, input().split()))
ans_max = 0
for i in range(n):
    ans = arr[i]-(n-i)
    if ans > ans_max:
        ans_max = ans
print(ans_max)