'''
    [문자열 비교]
        info리스트는 학생 정보이다.
        search리스트의 내용이 info에 있으면 o 없으면 x를 출력하시오. 
    [정답]
        이민수o
        김철수o
        김상진x
'''
info = ["김철수" , "이민수" , "유영희", "이민정", "조아라"]
search = ["이민수", "김철수", "김상진"]

# print(info)

# 0126
for i in range(len(search)) :

    ck = False
    for j in range(len(info)) :
        if search[i] == info[j] :
            ck = True
            break
    
    if ck == True :
        print(search[i], end = " O ")
    else :
        print(search[i], end = " X ")

      
# for i in range(len(search)) :
#     ck = False
#     for j in range(len(info)) :
#         if search[i] == info[j] :
#             ck = True 
#             break 
#     if ck == True :
#         print(search[i], "O")
#     else : 
#         print(search[i], "X")

# 정답
# for i in range(len(search)):

#     check = False
#     for j in range(len(info)):
#         if search[i] == info[j]:
#             check = True
#             break
    
#     result = search[i]
#     if check == True:
#         result += "O"
#     else:
#         result += "X"
#     print(result)

# 1212
# for i in range(len(search)) :
#     check = False
#     for j in range(len(info)) :
#         if search[i] == info[j] :
#             check = True
#             break 
    
#     result = search[i]
#     if check == True :
#         print(result,"O")
#     else :
#         print(result, "X")



