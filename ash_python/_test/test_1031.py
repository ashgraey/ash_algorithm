"""
[문제]
    철수는 5440미터를 가는데 1시간 12분이 걸렸다. 
    철수의 시속은 얼마인지구하시오.
    소수점 두자리로 구하시오.
[정답]
    4.53
"""
"""
속력 = 거리 / 시간

거리 = 5.44
시간 = 1 + 1 / 60
철수_1시간거리 = 거리 * 시간
철수_시속 = 철수_1시간거리 / 1

철수 1시간 이동거리
5.44 : 1.16 = x : 1
1.16x = 5.44 * 1
x = 5.44 / 1.16
"""
거리 = 5.44
시간 = 1 + 12 / 60
철수_1시간_거리 = 거리 / 시간
철수_시속 = 철수_1시간_거리 / 1
print(round (철수_시속, 2))

"""
[문제]
    철수는 시속3km의 속도로 2시간 21분을 걸었다.
    철수는 몇km를 걸었는지 구하시오.
    소수점 두자리로 구하시오.
[정답]
    7.05
"""
"""
거리 = 속력 * 시간
시속 = 3
분속 = 3 / 60
시간 = 60 * 2 + 21
거리 = 분속 * 시간
"""
시속 = 3
분속 = 3 / 60
시간 = (60 * 2) + 21
거리 = 분속 * 시간
print(round(거리, 2),"km")

"""
[문제]
    철수는 반장선거를 한다.
    전체인원 32명이다. 
    철수는 반장선거에서 7표를 받았다. 
    하였다. 몇퍼센트를 득표한것인지구하시오.
    소수점 두자리로 구하시오.
[정답]
    21.88
"""
"""
총원 = 32
철수_받은표 = 7
득표율 = x

32 : 100 = 7 : x
32x = 700
x = 700 / 32
"""
총원 = 32 
철수_받은표 = 7 
득표율 = 철수_받은표 * 100 / 총원
print(round(득표율, 2),"%")
