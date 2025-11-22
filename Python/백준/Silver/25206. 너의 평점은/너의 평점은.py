grade = {
    'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}

total_score = 0
total_grade = 0 #변수 설정

for i in range(20): #20줄 걸쳐 for문 실행
    user_input = input()
    subject, score_str, grade_str = user_input.split() #입력받기

    if grade_str.upper() == 'P':
        continue #Pass는 넘기기

    score_num = float(score_str) #평점을 숫자로 변환

    grade_num = grade.get(grade_str.upper()) #등급을 숫자로 변환

    total_score = total_score + (score_num * grade_num)
    total_grade = total_grade + score_num
    finally_score = total_score / total_grade

print('%.6f'%(finally_score))