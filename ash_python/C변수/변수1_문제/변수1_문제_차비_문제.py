'''
	[문제]
		철수는 집에서 학교까지 버스를 타고 다닌다.
		철수의 버스비는 1200원이다. 
		철수는 학교가 끝나면 바로 학원에 간다.
		학원에 갈 때는 지하철을 이용한다.
		지하철 요금은 1100원이다.
		철수가 학원에서 집으로 바로 올 때는 1300원의 차비가 든다.
		철수가 학교에서 집으로 바로 올 때는 1200원의 차비가 든다.
		학교는 월화수목금 매일 다닌다.
		학원은 월수금에만 다닌다.
		이번 달에 철수는 4주 동안 학교와 학원에 다녔다.
		이번 달 필요한 총차비를 구하시오.
		
	[정답] 
		62400
'''

bus = 1200
subway = 1100
HomeToEdu = 1300
HomeToSchool = 1200
WeekHomeToEdu = subway * 3 + HomeToEdu * 3
WeekHomeToSchool = bus * 5 + HomeToSchool * 2
WeekTransitionPay = WeekHomeToEdu + WeekHomeToSchool
print(WeekTransitionPay * 4)