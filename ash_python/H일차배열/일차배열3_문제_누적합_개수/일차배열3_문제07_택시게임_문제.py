'''
	[문제]	
		현재 택시는 5 , 5 위치에 있다. (y = 5 , x = 5)
		dir 배열은 뱡향을 뜻하고 [0, 1, 2 ,3] 은 [북, 동, 남, 서] 를 뜻한다. 	
		speed 배열은 속도를 뜻한다.	
		dir 과 speed 배열은 택시가 매번이동한 내용을 기록한 것이다. 	
		dir 과 speed 를 다 적용하면 y 와 x 는 어디에 와있는지 출력하시오. 
  
	[정답]
		dir = 3 , speed = 4 : 서쪽으로 4칸이므로 x에서 4를 뺀다. 
		dir = 2 , speed = 3 : 남쪽으로 3칸이므로 y에서 3을 뺸다.
		dir = 1 , speed = 1 : 동쪽으로 1칸이므로 x에서 1을 더한다.
		dir = 0 , speed = 2 : 북쪽으로 2칸이므로 y에서 2를 더한다.
		dir = 1 , speed = 3 : 동쪽으로 3칸이므로 x에서 3을 더한다. 

        y = 4
        x = 5
'''
y = 5
x = 5

dir = [3, 2, 1, 0, 1] # 방향(북0, 동1, 남2, 서3)
speed = [4, 3, 1, 2, 3]

# [1114]
# for i in range(len(dir)) :

# 	if dir[i] == 0 :
# 		y += speed[i]
# 	elif dir[i] == 1 :
# 		x += speed[i]
# 	elif dir[i] == 2 :
# 		y -= speed[i]
# 	elif dir[i] == 3 :
# 		x -= speed[i]

# print("x =",x) 
# print("y =",y) 

# [2차]
# for i in range(len(dir)) :

# 	# 북0
# 	if dir[i] == 0 :
# 		y += speed[i]
# 	# 동
# 	elif dir[i] == 1 :
# 		x += speed[i]
# 	# 서
# 	elif dir[i] == 2 :
# 		y -= speed[i]
# 	# 남
# 	elif dir[i] == 3 :
# 		x -= speed[i]

# print(x)
# print(y)

# [1차]
# for i in range(size) : 

# 	if dir[i] == 0 : 
# 		y += speed[i]
# 	if dir[i] == 1 : 
# 		x += speed[i]
# 	if dir[i] == 2 : 
# 		y -= speed[i]
# 	if dir[i] == 3 : 
# 		x -= speed[i]

# print("x =", x)
# print("y =", y)
	
