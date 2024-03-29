'''
   [문제]
      철수는 고속버스를 타고 여행을 떠나려 한다.
      출발시간까지 1시간 30분 여유가 있다.
      고속버스 역과 상점을 시속 3km로 걸어서 왕복하고,
      15분 동안 물건을 쇼핑하려고 한다.
      역에서 1.6km 떨어진 상점을 다녀올 수 있을지 구하시오.
   
      위 식을 표현하고, 풀이 과정을 주석으로 작성하시오.
'''
'''
거리 = 속력 * 시간 
시간 = 거리 / 속력

편도거리 * 2 / 철수분속 + 쇼핑시간 <= 여유시간
'''
print("-----문제1-----")
여유시간 = 90
편도거리 = 1.6
왕복거리 = 편도거리 * 2 
철수분속 = 3 / 60 
쇼핑시간 = 15

결과 = 왕복거리 / 철수분속 + 쇼핑시간
# print(결과)
print("철수가 상점에 다녀올수있는가? =", 결과 <= 여유시간)

'''
[문제] 		
    철수는 지금 모두의 마블 게임을 하고 있다.
    게임은 0 ~ 20까지 이동할 수 있는 거리가 있다.
    지금 철수의 차례이고 , 
    현재의 위치는 시작점으로부터 9만큼 이동했다.		 
    1 ~ 6의 눈금이 있는 주사위 2개를 던진다.
    주사위 숫자의 합만큼 이동한다. 
    아래 조건을 모두 만족하는 철수의 위치를 출력하시오.
        
    [조건]
    [1] 주사위 숫자의 합만큼 이동한다. 
        예) 3, 5 ==> 8 만큼 이동한다.

    [2] 단, 두 주사위 숫자가 둘다 짝수인경우는 숫자의 두배를 이동한다.
        예) 2, 2 ==> 4 + 4
		예) 5, 2 ==> 7

    [3] 14, 15, 16 번의 위치에 함정이 있다. 
        함정에 걸리면 다시 주사위 2개를 던지고 
        둘중 하나라도짝수이면 [페널티] 처음 위치(0)로 이동한다.
        둘다 홀수 라면 [페널티 없음] 함정을 탈출하여 다음 칸(17)으로 이동한다.

    [4] 20 이상의 값이 나오면 "승리"를 출력한다.
'''	
print("-----문제2-----")
import random

철수위치 = 9
print("철수 시작위치 =", 철수위치)

주사위1 = random.randint(1 , 6)
# 주사위1 = 4
print("주사위1 =", 주사위1) 
주사위2 = random.randint(1 , 6) 
# 주사위2 = 4
print("주사위2 =", 주사위2) 

합 = 주사위1 + 주사위2
# 철수위치 = 철수위치 + 합 
# print("다음 철수위치 =", 철수위치)
# if 주사위1 != 주사위2 : 
# 	철수위치 = 철수위치 + 합
# 	print(철수위치)
# if 주사위1 % 2 != 0 and 주사위2 % 2 != 0 :
# 	철수위치 += 합
# 	print("철수위치1 =",철수위치)

if 주사위1 % 2 == 0 and 주사위2 % 2 == 0 : 
	합 *= 2 
	철수위치 = 철수위치 + 합
	print("철수위치2 =",철수위치)

else :
	철수위치 = 철수위치 + 합
	print("철수위치1 =", 철수위치)


if 철수위치 == 14 or 철수위치 == 15 or 철수위치 == 16 : 
	print("함정에빠짐")
	주사위1 = random.randint(1,6) 
	print("주사위1 =",주사위1) 
	주사위2 = random.randint(1,6)
	print("주사위2 =",주사위2)

	if 주사위1 % 2 == 0 or 주사위2 % 2 == 0 : 
		철수위치 = 0
		print("페널티")
	
	if 주사위1 % 2 == 1 and 주사위2 % 2 == 1:
		print("페널티없음")
		철수위치 = 17

print("마지막 철수위치 =", 철수위치)
if 철수위치 >= 20 : 
	print("철수승리")
	 