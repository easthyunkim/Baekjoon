n = int(input())
s = input()
cnt = [s.count(i) for i in 'uospc']
print(min(cnt))