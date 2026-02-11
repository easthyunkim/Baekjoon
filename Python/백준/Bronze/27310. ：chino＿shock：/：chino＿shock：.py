s = list(input())
length = len(s)
colon = 0
under = 0
for i in s:
    if i == ':':
        colon += 1
    if i == '_':
        under += 1
print(length+colon+under*5)