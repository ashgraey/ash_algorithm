'''
    [문제]
        철수는 게임을 하고 있다. 
        monster는 게임의 적 4마리를 의미하고 9는 몬스터의 체력을 의미한다.
        철수의 공격력은 5이다.     
        랜덤으로 몬스터 중 하나를 선택해서 공격하고,
        이를 총 다섯 번 반복한다. 
        모든 몬스터를 공격한 후 몬스터들의 체력을 출력하시오.
        단, 몬스터 체력은 0이 되면 더 이상 내려가지 않는다. 
        또한 공격한 몬스터의 양쪽에게는 1의 대미지를 가하게 된다. 
        
'''
import random

monster = [9,7,8,6]
power = 5

# [1115]
# monster = [9,7,8,6]
# power = 5

# for i in range(5) :
#     r = random.randint(0, len(monster) - 1)
#     print("r =", r, end = " ")


#     if 0 < r < len(monster) - 1 : 
#         monster[r] -= power
#         monster[r + 1] -= 1 
#         monster[r - 1] -= 1
#     elif r == len(monster) - 1 :
#         monster[r] -= power
#         monster[r - 1] -= 1 
#     elif r == 0 :
#         monster[r] -= power
#         monster[r + 1] -= 1 

#     if monster[r] < 0 : 
#         monster[r] = 0
#         print("체력이 0")
   
#     print(monster)