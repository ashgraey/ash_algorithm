'''
	[문제]
		[1] a리스트의 값들을 순차적으로 검사한다. 
		[2] 연속으로 같은 값이 두 개가 있다면, 
		[3] 두 수를 삭제하고 그 합을 다시 그 자리에 저장한다.
		[4] 연속으로 같은 값이 없을 때까지 (1~3)을 반복한다.

		b = [8,4,2,2,8,4,4] 세번째 자리 2, 2가 연속이다.
		b = [8,4,4,8,4,4] , 두번째 자리 4, 4가 연속이다.
		b = [8,8,8,4,4] , 첫번째자리 8, 8 이 연속이다.
		b = [16,8,4,4] , 세번째자리 4, 4 이 연속이다.
		b = [16,8,8] , 두번째자리 8, 8 이 연속이다.
		b = [16,16] , 첫번째자리 16, 16 이 연속이다.
		b = [32] , 연속된 수가 없다. 
	[정답]
		b = [32, 0, 0, 0, 0, 0, 0]
'''
a = [8,4,2,2,4,4,8]
b = [0,0,0,0,0,0,0]
# b = []

# 1215
# 안되는건 계속 안됨
# cnt = 0
# for i in range(len(a) - 1) :
# 	if a[i] == a[i + 1] :
# 		a[i] = a[i] + a[i + 1]
# 		del(a[i + 1])
		
# 		# for j in range(len(b)) :
# 		# 	if a[j] != 0 :
# 		# 		b[j] = a[j]
	

# print(a)
# print(b)

# 1124
# 시도는 했지만 풀지못했다.
# i = 0
# while True :

# 	check = False
# 	j = i 
# 	while j < i + 2 :
# 		if i != j and a[i] == a[j] :
# 			check = True
# 			break  
# 		j += 1 

# 	if check == True : 
# 		a[i] += a[j]
# 		del(a[j])

# 	if i == len(a) :
# 		break
# 	i += 1	
# 	print(a)

