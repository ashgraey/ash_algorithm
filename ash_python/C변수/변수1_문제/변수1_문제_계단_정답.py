'''
	[문제]
		철수와 영희는 가위바위보 게임을 하고 있다. 
		규칙은 아래와 같다.	
		
		이기면 계단을 3칸 올라간다.
		비기면 계단을 1칸 올라간다. 
    지면  계단을 2칸 내려간다.
		
		철수는 4번 이기고, 2번 비기고, 3번 졌다.
		50번 계단에서 시작했을 때,
	 	철수는 몇 번째 계단에 있는지 구하시오.
	 	
	 [정답] 
        58
'''

현재위치 = 50

승리_횟수 = 4
폐배_횟수 = 3
무승부_횟수 = 2

현재위치 = 현재위치 + 승리_횟수 * 3 + 무승부_횟수 * 1 - 폐배_횟수 * 2
print(현재위치)
