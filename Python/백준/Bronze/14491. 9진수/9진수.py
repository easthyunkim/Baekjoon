w = int(input())
ans = ''
while w:
    ans += str(w%9)
    w //= 9
print(ans[::-1])