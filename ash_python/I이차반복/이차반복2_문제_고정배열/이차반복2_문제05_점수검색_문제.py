'''
	[문제]
		number 리스트는 학생 번호이고, score 리스트는 각 학생의 시험점수이다.
		search 리스트는 학생들이 시험 결과가 궁금해서 검색한 번호들이다. 
		각 학생이 검색한 순서대로 점수를 출력하시오.
	[정답]
		1002 : 65
		1004 : 1
		1003 : 23
		1001 : 4
		1005 : 45
		
'''
number = [1001, 1002, 1003, 1004, 1005, 1006]
score =  [4,    65,   23,   1,    45,   7]

search = [1002, 1004, 1003, 1001, 1005]

# 1123
# for i in range(len(search)) :
# 	for j in range(len(number)) :
# 		if search[i] == number[j] :
# 			print(number[j], ":", score[j])

# 1121
# for i in range(len(search)) :
# 	for j in range(len(number)) :
# 		if search[i] == number[j] :
# 			print(search[i], ":", score[j]) 