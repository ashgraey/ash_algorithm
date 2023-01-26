'''
	[상품주문]
		item 리스트는 상품의 번호이다.
		price 리스트는 상품의 가격이다.
		count 리스트는 상품의 재고개수이다.
		item과 price와 count 는 한세트이다.
  
		order 는 오늘 주문이들어온 상품의 인덱스 번호이다. 	
		단, 주문할때마다 count 재고에서 하나씩 감소하고, 재고가 0이면 주문할수없다.
		주문할수없을때는 "주문불가" 를 출력하시오.
		order 의 주문을 토대로 오늘 매출을 구하시오.
		count리스트도 출력하시오.
  
	[예시]
		count = [3, 1, 2, 1]
		(1) order = 0 , count = [2,1,2,1]
		(2) order = 1 , count = [2,0,2,1]
		(3) order = 3 , count = [2,0,2,0]
		(4) order = 3 , "주문불가"
		(5) order = 2 , count = [2,0,1,0]
		(6) order = 2 , count = [2,0,0,0]
		(7) order = 1 , "주문불가"
'''
item = [1001, 1002, 1003, 1004]
price =[500, 1200, 4300, 2300]
count = [3, 1, 2, 1]

order = [0, 1, 3, 3, 2, 2, 1]

total = 0

for i in range(len(order)) :
	if count[order[i]] > 0 :
		count[order[i]] -= 1 
		print(count)
	else :
		print(count, "주문불가")

print()
print(order)


