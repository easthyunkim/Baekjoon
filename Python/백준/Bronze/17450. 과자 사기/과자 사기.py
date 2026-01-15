lst = []
for i in range(3):
    price, weight = map(int, input().split())
    if price*10 >= 5000:
        price = price*10-500
    else:
        price *= 10
    weight *= 10
    lst.append(weight/price)
if max(lst) == lst[0]:
    print('S')
elif max(lst) == lst[1]:
    print('N')
else:
    print('U')