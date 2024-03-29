'''
	[문제]
		사탕 나눠주기 행사하고 있다. 
		병은 총 4병이고, 각 사탕 병의 개수는 각기 다르다.
		사탕은 한 사람당 25개씩 나눠주고 있다.
		count 리스트는 오늘 사탕을 나눠준 사람 수다.
		remainder 리스트는 사탕을 나눠주고 난 나머지이다.
		오늘 처음 가져온 사탕 수를 구하시오.

	[정답]
		candy = [80, 53, 36, 22]
	
		(1) count 는 3이니간 25를 곱하면 75 이고 나머지는 5이므로 원래는 80개이다.
			candy = [80]
   
		(2) count 는 2이니간 25를 곱하면 50 이고 나머지는 3이므로 원래는 53개이다.
			candy = [80, 53]
   
		(3) count 는 1이니간 25를 곱하면 25 이고 나머지는 11 이므로 원래는 36개이다.
			candy = [80, 53, 36]
   
		(4) count 는 0이니간 25를 곱하면 0 이고 나머지는 22이므로 원래는 22개이다.
			candy = [80, 53, 36, 22]
'''
'''
사탕 // 25 = 나눠준_수(count)
사탕 % 25 = 남은_수(remainder)
총 사탕 수 = count * 25 + remainder 
'''
candy = []
count =	[3, 2, 1, 0]
remainder = [5, 3, 11, 22]

candy_num = 25

# [1114]
# for i in range(len(count)) :
# 	candy.append((count[i] * 25) + remainder[i])

# print(candy)

# [2차]
# for i in range(len(count)) :
# 	총사탕 = (count[i] * candy_num) + remainder[i]
# 	candy.append(총사탕)

# print(candy)

# [1차]
# for i in range(len(count)) :
# 	total = count[i] * candy_num + remainder[i]
# 	candy.append(total)
	
# print(candy)
