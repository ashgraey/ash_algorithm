'''
[문제]
	철수는 오징어게임에 참가하였다.
	첫 번째 게임은 "무궁화꽃이 피었습니다" 이다.
	규칙은 아래와 같다.	
	[규칙]	
		[1] 전체 거리는 0 ~ 25까지 거리가 있다.
		[2] 철수는 현재 0의 자리에 있다.
		[3] 철수는 매 턴 1 ~ 4의 랜덤숫자를 뽑는다. 숫자만큼 이동한다. 
		[4]	이동 거리를 누적하며, 합이 25 이상이 되면 승리이며 종료한다.
		[5] 인형은 매턴 3 ~ 5의 랜덤숫자를 뽑는다. 
		[6] 인형보다 큰 숫자가 나오면 움직인 것으로 간주되어 패배하며 종료한다.
		[7] 10턴 안에 도착 못 하면 시간초과로 패배하며 종료한다.
		[8] 철수의 이동 경로를 전부 출력하시오.
'''
# [3차-1111]
# import random

# 거리 = 25 

# 철수 = 0
# 철수_합 = 0
# count = 0
# while True :
#     print("-----", count, "-----")
#     철수_이동 = random.randint(1, 4)
#     print("철수 이동 =", 철수_이동)
#     count += 1 

#     인형 = random.randint(3, 5)
#     print("인형 =", 인형)

#     철수_합 += 철수_이동
#     print("철수 이동경로 =", 철수_합)

#     if 철수_합 >= 거리 :
#         print("철수 승")
#         break
    
#     if 철수_이동 > 인형 :
#         print("움직임 철수 패배")
#         break

#     if count == 10 :
#         print("시간초과 패배")
#         break

# [2차]
# import random
# 철수_위치 = 0
# 전체거리 = 25 

# 철수_합 = 0
# 인형_합 = 0
# i = 0 
# while i < 10 :
#     철수 = random.randint(1, 4)
#     인형 = random.randint(3, 5)
#     print("철수 =", 철수)
#     print("인형 =", 인형)

#     철수_합 += 철수
#     print("철수 이동경로 =", 철수_합)
#     # 인형_합  += 인형 
#     if 철수_합 >= 전체거리 :
#         i = 10
#         print("철수 승리")
#         # run = 0 
#     if 철수 > 인형 :
#         # run = 0
#         i = 10
#         print("움직임 패배")
        
#     if 철수_합 < 25 and i > 9 :
#         print("시간초과 패배")
#     i += 1 

# [1차]
# chul = 0
# 이동 = 0
# count = 0
# run = 1 
# while run == 1 : 
# 	num = random.randint(1, 4)
# 	print(num)
# 	doll = random.randint(3, 5)
# 	print(doll)

# 	이동 += num
# 	print("이동한 거리 =", 이동)

# 	if 이동 >= 25 :
# 		print("승리")
# 		run = 0

# 	if num < doll :
# 		count += 1 

# 	if count < 10 :
# 		print("시간초과")
# 		run = 0

# 	if num > doll :
# 		print("패배")
# 		run = 0
	
