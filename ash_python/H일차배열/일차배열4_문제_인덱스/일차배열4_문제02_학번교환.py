'''
		
	[문제] 
		numberList 는 학생들의 번호를 저장한 리스트이다.
		scoreList 는 학생들의 점수를 저장한 리스트이다.
 		실수로 학생들의 점수가 한칸씩 밀렸다. 
		학생들의 점수를 한칸씩 앞으로 당기고 맨앞의 점수는 맨뒤에 저장하시오.
	
	[결과]	
		[ 1001, 1002, 1003, 1004, 1005 ];
		[ 11, 45, 98, 23, 87 ];
'''

numberList = [ 1001, 1002, 1003, 1004, 1005 ]
scoreList =  [ 87, 11, 45, 98, 23 ]

temp = scoreList[0]

for i in range(len(scoreList) - 1) :
	scoreList[i] = scoreList[i + 1]
	
scoreList[len(scoreList) - 1] = temp

print(scoreList)