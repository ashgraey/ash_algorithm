'''
  	[문제]
  		과일 상점에 과일 250개가 있다. 
  		그중에 오전에 120개가 팔렸고 오후에는 80개가 팔렸다.
  		남은 과일은 전체 과일의 몇 퍼센트인지 구하시오.
  		
  	[정답] 
  		20
'''

'''
	남은 과일 = 250 - (120 + 80) = 50

	250개 : 100% = 50개 : n%
	250n = 100 x 50
	n = 100 x 50 / 250
'''

전체과일_수 = 250

오전판매_수 = 120
오후판매_수 = 80
남은과일_수 = 전체과일_수 - 오전판매_수 - 오후판매_수

남은과일_퍼센트 = 남은과일_수 * 100 / 전체과일_수
print(남은과일_퍼센트)