'''
	[문제] 
		321321초를 시간을 제외한 "분"과,
        시간과 분을 제외한 "초"를 구한 후,	
		분과 초를 더한값이 100보다 큰지 확인하시오.

		위내용을 비교연산자로 표현하시오.
    [정답]
        False
'''

총시간 = 321321

분 = 총시간 % 3600 // 60
초 = 총시간 % 60

합 = 분 + 초

결과 = 합 > 100
print(합)
print(결과)