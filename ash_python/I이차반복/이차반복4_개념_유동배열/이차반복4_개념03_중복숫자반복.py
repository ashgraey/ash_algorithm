'''
	[문제]
		a리스트에 랜덤(1~4) 숫자 4개를 저장한다. 
		단, 중복없는 숫자로 저장한다.
	
	[예시]
		[1,4,2,3]
'''
import random

a = []

# 정답
# count = 0
# while True:
# 	r = random.randint(1,4)
# 	check = False
# 	# 중복숫자체크
# 	for i in range(len(a)):
# 		if a[i] == r:
# 			check = True
# 			break
	
# 	if check == False:
# 		a.append(r)
# 		count += 1 
	
# 	if count == 4 :
# 		break

# print(a)

# 1123
# 개념이해가 완벽하진않음
# count = 0 
# while True : 
# 	r = random.randint(1,4)

# 	check = False
# 	for i in range(len(a)) :
# 		if a[i] == r :
# 			check = True
# 			break
	
# 	if check == False :
# 		a.append(r)
# 		count += 1 
	
# 	if count == 4 : 
# 		break
# print(a)