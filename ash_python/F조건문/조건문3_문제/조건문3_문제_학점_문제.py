'''
    [문제]
        0에서 100 사이의 랜덤 숫자를 시험 점수로 저장한다.
        시험점수에 해당하는 학점을 출력하시오.
        아래는 점수표이다.
        100~91 이면 A학점,
        90~81  이면 B학점,
        80 이하는 "재시험"
        
        단, 만점이거나, A 학점과 B 학점의 일의 자리가 8점 이상이면 + 기호를 추가하시오.
        [예] 
            100 => A+
            88 ==> B+
            82 ==> B
            23 ==> 재시험
'''
import random

# 점수 = 1
점수 = random.randint(0, 100)
print("점수 =", 점수)
일 = 점수 % 10

# if 점수 == 100 :
#     print("A+")

resul = 0 
if 100 >= 점수 > 90 and 일 >= 8:
    print("A+")
if 98 > 점수 >= 90 :
    print("A")
if 90 > 점수 > 80 and 일 >= 8 :
    print("B+")
if 88 > 점수 >= 80 : 
    print("B")
if 점수 < 80 :
    print("재시험")


    