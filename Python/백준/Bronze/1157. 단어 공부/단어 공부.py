word = input().upper()
word_list = list(set(word))
list = []

for i in word_list:
    cnt = word.count(i) #단어 세기
    list.append(cnt) #리스트에 넣기

if list.count(max(list)) >= 2:
    print('?')
else:
    print(word_list[list.index(max(list))])