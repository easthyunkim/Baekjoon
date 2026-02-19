s = input()
stack = []
ans = 0
tmp = 1

for i in range(len(s)):
    if s[i] == '(': #case_1
        stack.append(s[i])
        tmp *= 2

    elif s[i] == '[': #case_2
        stack.append(s[i])
        tmp *= 3

    elif s[i] == ')': #case_3
        if not stack or stack[-1] == '[': #not_fair_1
            ans = 0
            break
        if s[i-1] == '(': #is_pair_1
            ans += tmp
        stack.pop()
        tmp //= 2 #tmp_reset_1

    else: #case_4
        if not stack or stack[-1] == '(': #not_fair_2
            ans = 0
            break
        if s[i-1] == '[': #is_pair_2
            ans += tmp
        stack.pop()
        tmp //= 3 #tmp_reset_2

if stack: #remain
    print(0)
else: #not_exist
    print(ans)