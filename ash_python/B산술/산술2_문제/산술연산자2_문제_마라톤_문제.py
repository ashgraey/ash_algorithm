'''
	[문제]
		민수는 마라톤을하면서 2시간 3분 동안 13828m 를 달렸다.
	   	3분동안 간거리는 얼마인지 구하시오.
	   	소수점 두자리까지 구하시오.
	   	
	   	[정답] 337.27
'''
one_min_distance = 13828 / 123
three_min_distance = round(one_min_distance * 3, 2)
print(three_min_distance)
