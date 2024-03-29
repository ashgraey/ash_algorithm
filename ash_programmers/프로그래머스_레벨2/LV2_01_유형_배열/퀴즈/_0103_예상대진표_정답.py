# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    c = 0  
    if a > b:
        temp = a 
        a = b 
        b = temp
    while True:
        c += 1
        if a % 2 == 1 and a + 1 == b:
            break
        
        if a % 2 == 1:
            a = a + 1
        a = a // 2
        if b % 2 == 1:
            b = b + 1
        b = b // 2


    return c


N = 8
A = 4
B = 7
r = solution(N , A , B)
print(r)

"""
a와 b가 만나기위해서는
항상 a가 작다고 했을때,
a는 홀수이고 b는 a + 1 이여야한다. 
예를 들면 [1,2][3,4][5,6][7,8] 이런식이다. 
진사람들은 사라지고 새로운번호를 받게되니, 
반으로 나눈거와같다. 단 홀수는 나눠지지않으니 1을 더해준다. 

[1] a 가 홀수이고 b가 a + 1 이될때까지 
[2] a 나누기 2  , b 나누기 2 를 한다. 
[3] 단 , a나 b가 홀수이면 나눠지지않으니 + 1을 해준다

==============================================
[1] a는 4 이고 b 7 이니 b는 + 1을 한다. 
[2] 다시 반으로 나눠준다. 
[3] a = 2 가되고 b = 4 가된다.
[4] 다시 반으로 나눠준다. 
[5] a = 1 이되고 b = 2 가된다. 
[6] a는 홀수이고 b는 a + 1 이므로 서로 만났다. 
"""