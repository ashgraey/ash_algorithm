'''
	[문제] 
		numberList는 학생들의 번호를 저장한 리스트이다.
		scoreList는 학생들의 점수를 저장한 리스트이다.
 		랜덤으로 한 학생의 학번과 점수를 출력하시오.
   
	[예시1] 
        r = 0
		1001 , 87
  
	[예시2]
        r = 3
		1004 , 97
'''
import random

numberList = [1001, 1002, 1003, 1004, 1005]
scoreList =   [87, 11, 45, 98, 23]

# [1115]
# r = random.randint(0, len(numberList) - 1)
# print("r =", r)
# print(numberList[r], scoreList[r])

# [2차]
# size = len(numberList) - 1 
# r = random.randint(0, size)
# print("random =", r)
# print(numberList[r],",",scoreList[r])

# [1차]
# r = random.randint(0, len(numberList) - 1)
# print("r =", r)
# print(numberList[r],",",scoreList[r])




