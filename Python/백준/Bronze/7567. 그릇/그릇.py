dish = list(str(input()))
ans = 0

for i in range(len(dish)):
    if i == 0: #처음상태
        ans += 10
    elif dish[i] == dish[i-1]: #겹친상태
        ans += 5
    else: #안겹친상태
        ans += 10

print(ans)