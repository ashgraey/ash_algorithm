'''
	[문제]
		(1) 랜덤(1 ~ 9) 사이의 랜덤값을 4개를 저장 후 비교한다. 
		(2) 4개의 랜덤값이 모두 홀수이면 1을 total에 추가,
			하나라도 홀수가 아니면 2를 total에 추가한다.
		(3) (1~2)를 5번 반복한다. 

		[예시] 
			[3, 1, 5, 1] 모두홀수 => total = [1]
			[5, 2, 1, 4] 모두홀수x => total = [1,2]
			...
'''
import random 

total = []

# [1122]
# i = 0 
# while i < 5 : 
# 	r = []
# 	count = 0
# 	for j in range(4) :
# 		r.append(random.randint(1, 9))
# 		print(r)

# 		if r[j] % 2 == 1 :
# 			count += 1
# 			# print(count)
# 	if count == len(r) :
# 		total.append(1)
# 	else :
# 		total.append(2)
# 	i += 1 
		
# print("total =", total)

