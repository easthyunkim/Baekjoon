N = int(input())
str = input()
str_cnt = []

for i in str:
    if i != ',' and i != ' ':
        str_cnt.append(str.count(i))

print(max(str_cnt))