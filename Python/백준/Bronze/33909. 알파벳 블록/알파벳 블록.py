s, c, o, n = map(int, input().split())
s += n
o += c/2
print(int(min(s/3, o/3)))