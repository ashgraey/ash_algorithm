'''
    [문제]
        숫자 10과 3을 각각 저장한다.
        랜덤으로 0~3 저장한다. 랜덤숫자는 연산자에 해당하고,
        각각의 숫자는 다른 연산자를 뜻한다. 
        (0 은 +, 1 은 -, 2는 *, 3은 / )
        숫자10과 3을 연산해주는 함수들과 식을 만드시오.
        위 식을 5번 반복하시오.
    [예시]
       r = 3
       3은 / 이므로 10 / 3 
'''
import random

def calculator(r) :
    print("r : ", r)
    x = 10
    y = 3
    result = 0
 
    if r == 0 : 
        result = y + x

    elif r == 1 : 
        result = y - x
    
    elif r == 2 :
        result = y * x

    elif r == 3 :
        result = y / x
    
    return result

result = calculator(random.randint(0, 3))
print("result : ", result)