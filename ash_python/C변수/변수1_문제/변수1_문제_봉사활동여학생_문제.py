'''
	[문제]
   		철수네 반 학생은 30명이다.
   		남학생은 16명이다.
   		이 중에서 남학생은 3명 , 
   	 	여학생은 남학생의 3배의 학생이 봉사활동을 하였다.
    	봉사활동을 하지 않은 여학생은 몇 명인지 구하시오.
    	
  	[정답] 
  		5
'''

class_tot = 30
class_boy = 16
class_girl_service = 3 * 3
print(class_tot - (class_boy + class_girl_service))