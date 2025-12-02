L = int(input())
word = input()
mod = 1234567891
ans = 0

for i in range(L):
    hash = ord(word[i])-96 #아스키 코드에서 96을 빼면 된다고 하네요
    ans += hash*31**i

print(ans%mod)