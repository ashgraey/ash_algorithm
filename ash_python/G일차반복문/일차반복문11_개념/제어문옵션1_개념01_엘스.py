'''
[조건문 옵션 else]
    [1] 조건문 if 의 옵션이며, 단독으로 사용할 수 없다. 
    [2] if 조건이 거짓일 때 동작한다.
'''
'''
[문제]
    변수 a의 값이 홀수이면 "홀수", 짝수이면 "짝수" 를 출력하시오. 
'''
# [사용법]

a = 11

# if a % 2 == 1 : 
#     print("홀수")
# else : 
#     print("짝수")

if a % 2 == 0:
    print("짝수")
if a % 2 == 1:
    print("홀수")

print("-------")

if a % 2 == 0:
    print("짝수")
else:
    print("홀수")