'''
	[문제]
		사과 8개의 무게는 1056g이다.
		배 1개는 사과 1개의 117%의 무게를 갖고 있다.
		사과 5개 배 7개를 구입하였다. 
		과일전체의 총무게를 구하시오. 
		소수점 두 자리까지 구하시오.
		
	[정답]
		1741.08
'''

사과8개_무게 = 1056
사과1개_무게 = 사과8개_무게 / 8

배1개_무게 = 사과1개_무게 * 1.17

총무게 = 사과1개_무게 * 5 + 배1개_무게 * 7
print(총무게)