#입력받기
N = int(input())
words = input().split()
ans = [i + "DORO" for i in words]

#출력하기
print(' '.join(ans))