'''
    [문제]
        a리스트에는 이미 1~3의 값이 저장되어 있다.
        이제 추가로 랜덤(1~10)을 10번 추가하려 한다. 
        단, 중복숫자가 있으면 저장하지 않는다.
    [예시]
        [1, 2, 3, 10, 8, 9, 4]
'''
import random

a = [1,2,3]

# 정답
# i = 0
# while i < 10:
#     r = random.randint(1, 10)

#     check = False
#     j = 0
#     while j < len(a):
#         if r == a[j]:
#             check = True
#             break
#         j += 1
    
#     if check == False:
#         a.append(r)
#     i += 1

# print(a)

# 1124
# 방법1
# i = 0
# while i < 10 :
#     r = random.randint(1, 10)
#     check = False 

#     j = 0
#     while j < len(a) : 
#         if r == a[j] :
#             check = True
#             break
#         j += 1 
    
#     if check == False :
#         a.append(r)
#         # print(len(a))
#     i += 1 
# print(a)
#----------
# 방법2
# count = 0
# while True :
#     r = random.randint(1, 10) 
#     check = False

#     for j in range(len(a)) :
#         if r == a[j] :
#             check = True
#             break
    
#     if check == False :
#         a.append(r)
    
#     count += 1 
#     if count == 10 : 
#         break
# print(a)

# 1122
# i = 0  
# while i < 10  :

#     r = random.randint(1, 10) 
#     check = False
    
#     j = 0 
#     while j < len(a) :
#         if a[j] == r : 
#             check = True
#             break
#         j += 1 

#     if check == False : 
#         a.append(r)
        
#     i += 1 
# print(a) 
    
