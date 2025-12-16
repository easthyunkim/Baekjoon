import datetime
dt = datetime.datetime(2014, 4, 2)
N = int(input())
anni = dt+datetime.timedelta(days=N-1)
print(anni.strftime("%Y-%m-%d"))