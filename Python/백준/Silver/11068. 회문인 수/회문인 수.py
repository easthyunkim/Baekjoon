T = int(input())
for i in range(T):
    s = int(input())
    flag = False
    for j in range(2, 65):
        val = []
        x = s
        while True:
            if x == 0:
                break
            val.append(x%j)
            x //= j
        pd_flag = True
        for k in range(len(val)//2):
            if val[k] != val[-1-k]:
                pd_flag = False
        if pd_flag == True:
            flag = True
    if flag == True:
        print(1)
    else:
        print(0)