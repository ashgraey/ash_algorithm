'''
	[문제]
		현금이 10000원을 가지고,
		가격이 1200원인 과자 6개를 구입 후 거스름돈을 구하시오.
		단, 과자를 3개를 구입할 때마다 200원씩 할인해주는 행사를 진행 중이다. 
		
	[정답] 
		3200
'''

cash = 10000
price = 1200
discount = (6 // 3) * 200

change = cash - (price * 6) + discount
print(change)