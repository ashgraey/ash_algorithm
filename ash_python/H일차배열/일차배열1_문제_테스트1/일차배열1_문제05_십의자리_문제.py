'''
    [문제]
        a 리스트에서 십의자리가 2인 수만 출력하시오.
    [정답]
        423
        124
'''

a = [510,423,124,512,252,23,312,453,122]

# [1114]
# for i in range(len(a)) :
#     if a[i] % 100 // 10 == 2 :
#             print(a[i])
# [2차]
# for i in range(len(a)) :
#     십자리 =a[i] % 100 // 10
#     if 십자리 == 2 :
#         print(a[i])

# [1차]
# for i in range(len(a)) :
#     if a[i] % 100 // 10 == 2 :
#         print(a[i], end = " ")
