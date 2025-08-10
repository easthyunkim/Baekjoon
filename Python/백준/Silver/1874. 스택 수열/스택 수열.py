import sys
N = int(sys.stdin.readline())
stack = []
answer = []
check = True
count = 1
for i in range(N) :
    num_input = int(sys.stdin.readline())
    while num_input >= count :
        stack.append(count)
        answer.append('+')
        count += 1
    if stack[-1] == num_input :
        stack.pop()
        answer.append('-')
    else :
        check = False
if check :
    for j in answer :
         print(j)
else :
        print('NO')