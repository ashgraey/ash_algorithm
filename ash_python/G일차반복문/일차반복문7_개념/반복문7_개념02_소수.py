'''
[문제]
	10~100 사이의 랜덤 숫자를 저장하고, 해당 숫자가 소수인지 아닌지 판별하시오.
	소수란, 1과 자기 자신으로만 나눠지는 수를 의미한다.
	예) 2, 3, 5, 7, 11, 13, ..		

	(1) 해당 숫자를 1부터 자기 자신까지 나눈다.
	(2) 나머지가 0일 때마다 카운트를 센다.
	(3) 그 카운트 값이 2이면 소수이다.
	(4) 6/1 6/2 6/3 6/4 6/5 6/6	==> count=4	==> (소수x)
	(5) 2/1 2/2 	==> count=2	==>(소수)
[예시]
	53
	소수이다.
'''
import random

r = random.randint(1 , 100)
print(r)

# size = 100
count = 0
i = 1
# 소수인지 점검
while i <= r :
	if r % i == 0 :
		count += 1 
	i += 1 

# count변수를 활용하여 소수만 출력하는 조건
if count == 2 :
	print("소수이다.")
	# 소수 = i
if count != 2 :
	print("소수가 아니다.")
	# 소수 = i


# num = random.randint(10, 100)
# print("num =", num)

# count = 0

# i = 1
# while i <= num:
# 	if num % i == 0:
# 		count += 1

# 	i += 1

# if count == 2:
# 	print("소수이다.")
# if count != 2:
# 	print("소수가 아니다.")



