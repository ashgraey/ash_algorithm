'''
	[문제]
		랜덤(2~10)의 숫자를 저장하고 랜덤개수만큼 반복을 하면서 반복숫자를 저장한다.
		반복숫자란? 1 2 3 1 2 3 1 2 3 을 반복해서 저장하는것이다.
	[예1] 
		r = 8
		arr = [1,2,3,1,2,3,1,2];
  
	[예2] 
		r = 4
		arr = [1,2,3,1];
'''
import random

arr = []

r = random.randint(2, 10)
print("r =", r)

value = 1 

for i in range(r) :
	arr.append(value)
	value += 1 

	if i % 3 == 2 :
		value = 1
	
print(arr)
