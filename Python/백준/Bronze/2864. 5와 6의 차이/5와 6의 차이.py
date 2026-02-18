import sys
input = sys.stdin.readline

def min_cnt(x):
    ans = ''
    for i in x:
        if i == '6':
            ans += '5'
        else:
            ans += i
    return ans

def max_cnt(x):
    ans = ''
    for i in x:
        if i == '5':
            ans += '6'
        else:
            ans += i
    return ans

a, b = input().split()

minans = int(min_cnt(a))+int(min_cnt(b))
maxans = int(max_cnt(a))+int(max_cnt(b))

print(minans, maxans)