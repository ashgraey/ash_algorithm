'''
    [경마]
        horse_race리스트는 경마 게임을 표현한 것이다. 
        숫자 1~5는 말 번호를 뜻한다.               
        한 번에 말들은 2~5칸을 랜덤으로 이동한다.
        모든 말이 도착할 때까지 말의 이동 경로를 출력하시오.     
        rank리스트에 등수를 저장하시오.
    [예시]
        주사위 : [2,4,2,1,3] 이나왔다고하면, 아래와 같이 된다. 
    
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
'''
import random
horse_race = [
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
rank = [0,0,0,0,0]

position = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
total = [0, 0, 0, 0, 0]

# 1212 답보고도 이해못함;;
# while True : 
#     dice = []
#     for i in range(5) :
#         dice.append(random.randint(2, 5))

#     print(dice)

#     for i in range(len(dice)) :
#         horse_race[i][dice[i]] = i + 1
