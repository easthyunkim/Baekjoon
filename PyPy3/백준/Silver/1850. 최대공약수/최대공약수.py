import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
print('1'*(math.gcd(a, b)))