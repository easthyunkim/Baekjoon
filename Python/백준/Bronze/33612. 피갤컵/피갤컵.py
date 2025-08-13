N = int(input())
Y = 2024
M = 1
month = N*7
M += month
if M % 12 == 0:
    Y += (M//12)-1
    M = 12
else :
    Y += (M//12)
    M %= 12
print(Y, M)