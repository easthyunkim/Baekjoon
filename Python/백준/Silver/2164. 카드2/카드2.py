import sys
from collections import deque #덱으로 풀기
input = sys.stdin.readline

N = int(input())
card = deque([i for i in range(1, N+1)]) #입력받기

while (len(card) > 1): #마지막 카드가 남을 때 까지
    card.popleft() #제일 위에 있는 카드 버리기
    move_card = card.popleft() #그 다음 위에 있는 카드
    card.append(move_card) #맨 뒤로 옮기기

print(card[0]) #남는 카드 번호 출력