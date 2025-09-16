N = input()
list = [0]*10
for i in N:
    if i == '9' or i == '6':
        if list[9] <= list[6]:
            list[9] += 1
        else:
            list[6] += 1
    else:
        list[int(i)] += 1
print(max(list))