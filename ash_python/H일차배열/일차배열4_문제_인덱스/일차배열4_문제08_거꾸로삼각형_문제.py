'''
	  	[문제]
		 	아래 리스트를 아래와 같이 출력하시오.
		[결과]
			1234
			567
			89
			0
'''
'''
1234 3
567 6
89 8
0 0 
'''



a = [1,2,3,4,5,6,7,8,9,0]

start = 0
end = 4
for i in range(len(a)) :
	print(a[i], end = " ")
	start += 1 

	if start == end : 
		start = 0
		end -= 1
		print()
	

