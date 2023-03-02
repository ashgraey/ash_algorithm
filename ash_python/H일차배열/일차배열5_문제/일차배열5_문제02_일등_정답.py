'''
	[문제]
		다음은 학생 번화와 점수의 한 세트이다.
		일등의 번호와 점수, 꼴등의 번호와 점수를 출력하시오.
	[정답]
		일등 = 1004 98
		꼴등 = 1002 11
'''


numberList = [1001, 1002, 1003, 1004, 1005]
scoreList = [87, 11, 45, 98, 23]

maxScore = 0
maxIndex = 0

minScore = 100
minIndex = 0

for i in range(len(numberList)):
	if maxScore < scoreList[i]:
		maxScore = scoreList[i]
		maxIndex = i
	if minScore > scoreList[i]:
		minScore = scoreList[i]
		minIndex = i

print("일등 =", numberList[maxIndex], maxScore)
print("꼴등 =", numberList[minIndex], minScore)
