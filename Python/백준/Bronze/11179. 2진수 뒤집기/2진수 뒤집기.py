N = int(input())
binary = bin(N)[2:]
bin_reverse = binary[::-1]
print(int(bin_reverse, 2))