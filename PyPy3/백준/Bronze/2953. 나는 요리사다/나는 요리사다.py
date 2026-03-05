cnt_arr = cnt_s = 0
for i in range(5):
    s = sum(map(int, input().split()))
    if s > cnt_arr:
        cnt_arr = s
        cnt_s = i+1
print(cnt_s, cnt_arr)