'''
[문제]
	민수네 반 학생은 26명이다.
	민수네반 학생들에게 도화지를 두 장씩 나누어 주려 한다.
	도화지는 열 장씩 묶음으로만 판매하고 있고, 한 묶음에 1200원이다.
	총 얼마가 필요한지 구하시오.
[정답]
	7200원
'''

학생 = 26
도화지 = 학생 * 2
도화지_가격 = 1200
도화지_묶음 = 10

민수_도화지묶음 = 도화지 // 도화지_묶음
if 도화지 % 도화지_묶음 != 0 :
	민수_도화지묶음 += 1

필요금액 = 도화지_가격 * 민수_도화지묶음
print(필요금액)


# 학생 = 26
# 필요한_도화지_개수 = 학생 * 2
# 돈 = 0

# # 묶음 = 총개수 // 개수의 단위(10, 100, 1000...)
# 묶음 = 필요한_도화지_개수 // 10
# # 조건 : 개수의 단위가 0으로 떨어지지 않을경우 1묶음이 추가로 더 필요하기 때문에
# # 총개수 % 개수의 단위(10, 100, 1000..) -> 나머지의 값이 0보다 크면 묶음 = 묶음 + 1이 된다.
# if 필요한_도화지_개수 % 10 > 0:
#     묶음 = 묶음 + 1

# 돈 = 묶음 * 1200
# print("돈 : ", 돈)
