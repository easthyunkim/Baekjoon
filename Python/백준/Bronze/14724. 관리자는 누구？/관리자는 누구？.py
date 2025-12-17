N = int(input())
dict = {}
circle = ['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN',
          'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY']

for i in range(9):
    K = list(map(int, input().split()))
    dict[circle[i]] = max(K) #최고값 뽑기

most = list(dict.values()) #value값 추출
max_most = most.index(max(most)) #인덱스 추출
print(circle[max_most])