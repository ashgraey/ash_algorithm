'''
	[문제]
		철수는 친구의 생일 선물로 가격이 4000원인 필통 1개와 
		가격이 700원인 공책 몇권을 사려고 한다. 
		철수는 13000원을 가지고있을때,
		공책은 최대한 몇권을 살수있을지 구하시오.
		공책을 최대로 구입한후 나머지금액도 출력하시오.
		
	[정답] 
		12
        600
'''
pencil_case = 4000
book = 700
pay = 13000 - pencil_case
book_cnt = pay // book
book_change = pay % book
print(book_cnt, book_change)