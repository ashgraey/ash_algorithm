'''
    [문제]
        1. 1~100까지 반복한다.
        2. 각 수에 3이나 6이나 9의 개수를 누적해서 출력하시오. 

        [예시]
            3 1
            6 1
            9 1
            13 1
            16 1
            ...
            98 1
            99 2
'''
i =  1
while i <= 100 :
    일의자리 = i % 10
    십의자리 = i // 10
   
    count = 0
    if 일의자리 == 3 or 일의자리 == 6 or 일의자리 == 9 :
         count += 1
    
    if 십의자리 == 3 or 십의자리 == 6 or 십의자리 == 9 :
        count += 1    
    
    if count == 2 :
        print(i, "2")
    if count == 1 :
        print(i, "1")
    if count == 0 :
        print(i)

    i += 1 
    
# count = 0
# i = 1 
# while i <= 100 : 
#     if i % 3 == 0 or i % 6 == 0 or i % 9 == 0 : 
#         count += 1 
    
#         if count == 1 : 
#             print(i, count)

#         if count == 2 : 
#             print(i, count)

#     i += 1 

# [정답]
# i = 1
# while i <= 100:
#     x = i // 100
#     y = i % 100 // 10
#     z = i % 10

#     count = 0
#     if x == 3 or x == 6 or x == 9:
#         count += 1
#     if y == 3 or y == 6 or y == 9:
#         count += 1
#     if z == 3 or z == 6 or z == 9:
#         count += 1
    
#     if count > 0:
#         print(i, count)

#     i += 1