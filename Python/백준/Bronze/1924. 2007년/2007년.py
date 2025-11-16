day = 0
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
x, y = map(int, input().split()) #입력받기

for i in range(x-1):
    day += month[i] #달의 일수 추가
day = (day+y)%7 #일의 일수 추가 후 1주일로 나누기

print(week[day]) #출력하기