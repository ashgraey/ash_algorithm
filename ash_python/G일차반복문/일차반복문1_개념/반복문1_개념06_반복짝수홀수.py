'''
[문제] 아래 조건을 만족하는 식을 작성하시오.
		[조건1] 1~10까지 반복문을 활용해서 숫자를 출력한다.
		[조건2] 숫자가 홀수일때는 숫자 대신 "홀수"를 출력한다.		
[정답]
	홀수
	2
	홀수
	4
	홀수
	6
	홀수
	8
	홀수
	10
'''

i = 1
while i <= 10:
	# 홀수 일 때
	if i % 2 == 1:
		print("홀수")
	# 짝수 일 때
	if i % 2 == 0:
		print(i)
	i += 1









