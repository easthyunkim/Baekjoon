n = int(input())
dict = {'A':'000000', 'B':'001111', 'C':'010011', 'D':'011100',
        'E':'100110', 'F':'101001', 'G':'110101', 'H':'111010'}
arr = input()
key = list(dict.keys())
val = list(dict.values())
cnt_word = 0
ans = []

for i in range(0, len(arr), 6):
    a = arr[i:i+6]
    cnt_word += 1
    if a in val:
        for j in range(8):
            if a == val[j]:
                ans.append(key[j])
    else:
        cnt_total_error = 0
        for k in range(8):
            cnt_error = 0
            for l in range(6):
                if a[l] != val[k][l]:
                    cnt_error += 1
            if cnt_error <= 1:
                ans.append(key[k])
                break
            else:
                cnt_total_error += 1
        if cnt_total_error == 8:
            break

if len(ans) == n:
    print(''.join(ans))
else:
    print(cnt_word)