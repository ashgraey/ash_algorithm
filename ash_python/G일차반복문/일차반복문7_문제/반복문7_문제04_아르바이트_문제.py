'''
	[문제]
		철수는 편의점에서 아르바이트한다.
		한 달 동안 요일 구분 없이 이틀 연속 출근 후 
        하루 휴무 이렇게 반복 근무한다. 
		이번 달은 30일까지 있고 1일(월요일)이 출근 첫날이라고 하면,
		이번 달 철수가 출근하는 날짜와 요일을 전부 출력하시오.
	[정답]
        1 월
        2 화
        4 목
        5 금
        7 일
        8 월
        10 수
        11 목
        13 토
        14 일
        16 화
        17 수
        19 금
        20 토
        22 월
        23 화
        25 목
        26 금
        28 일
        29 월
'''
한달 = 30

unit = 0
i = 1
while i <= 한달 :
    
    unit = i % 7 

    if i % 3 != 0 : 
        print(i, end = " ")
    
        if unit == 1 :
            print("월요일")
        if unit == 2 :
            print("화요일")
        if unit == 3 :
            print("수요일")
        if unit == 4 :
            print("목요일")
        if unit == 5 :
            print("금요일")
        if unit == 6 :
            print("토요일")
        if unit == 0 :
            print("일요일")
    i += 1 


# 한달 = 30
# unit = 0

# i = 1
# while i <= 한달 : 
#     unit = i % 3 

#     if unit % 2 == 0 : 
#         print(i)
#     i += 1 