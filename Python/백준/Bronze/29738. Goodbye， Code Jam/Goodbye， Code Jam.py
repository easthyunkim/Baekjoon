T = int(input()) 
for i in range(0, T):
    N = int(input()) 
    rnd = 'Round 1' #입력받기

    if N <= 25:
        rnd = 'World Finals'
    elif N <= 1000:
        rnd = 'Round 3'
    elif N <= 4500:
        rnd = 'Round 2' #경우의 수 분기하기

    print(f"Case #{i+1}: {rnd}") #출력하기