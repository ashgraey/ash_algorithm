'''
    [문제]
        a리스트와 count리스트는 본래 한 쌍의 데이터로
        원래 한 줄로 되어있는 데이터를 두 개의 리스트로 압축해 놓은 것이다.
        원래대로 압축을 풀려고 한다.

        a리스트의 값은 저장할 숫자이고 
        count리스트의 값은 a리스트 값의 개수이다.
        예를 들어 a는 3이고 count는 5이므로 33333이다.

        남은 모든 경우도 압축을 풀고 b리스트에 저장하고, 출력하시오.
    [정답] 
        b = [3,3,3,3,3,5,5,5,5,5,5,2,4,4,4]
'''
a = [3,5,2,4]
count = [5,6,1,3]

b = []

# 1124
# for i in range(len(a)) :
#     for j in range(count[i]) :
#         b.append(a[i])
# print(b)

# 1122
# for i in range(len(a)) :
#     for j in range(count[i]) :
#         b.append(a[i])

# print(b)