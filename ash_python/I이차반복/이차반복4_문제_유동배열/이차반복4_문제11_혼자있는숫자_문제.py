'''
	[문제]
		a리스트에서 혼자있는 숫자만 출력하시오.
	[정답]
		20 50
'''

a = [10,20,30,40,40,10,30,10,50]

# 1124
# for i in range(len(a)) :
# 	check = False

# 	for j in range(len(a)) :
# 		if i != j and a[i] == a[j] :
# 			check = True
# 			break
	
# 	if check == False :
# 		print(a[i], end = " ")

# 1122
# for i in range(len(a)) :
# 	count = 0 
# 	for j in range(len(a)) :
# 		if i != j and a[i] == a[j] : 
# 			count += 1 
		
# 	if count == 0 : 
# 		print(a[i], end = " ")
	