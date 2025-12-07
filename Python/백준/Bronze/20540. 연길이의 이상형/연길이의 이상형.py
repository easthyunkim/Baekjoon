A = input()
MBTI = ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']
for i in A:
    MBTI.remove(i)
print(''.join(MBTI))