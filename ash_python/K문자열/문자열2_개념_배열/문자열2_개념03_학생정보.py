student = [
		["번호",  "이름", "성별", "국어", "수학"],
		[1001, 	"이만수",  "남",     10,     20],
		[1002,  "이영희",  "여",     70,     30],
		[1003,  "김민정",  "여",     64,     65],
		[1004,  "이철민",  "남",     13,     87],
		[1005,  "오만석",  "남",     49,     80],
		[1005,  "최이슬",  "여",     14,     90]
	]

'''
	[문제3] 
		국어 점수가 수학 점수 보다 큰 학생들의
		번호, 이름을 출력하시오.
	[정답3]
		1002 이영희
'''
print("[문제3]")
# 정답
# i = 1
# while i < len(student):
# 	if student[i][3] > student[i][4]:
# 		print(student[i][0], student[i][1])
# 	i += 1

# i = 1 
# while i < len(student) :
# 	if student[i][-2] > student[i][-1] :
# 		print(student[i][0], student[i][1])
		
# 	i += 1 

for i in range(1, len(student)) :
	if student[i][-2] > student[i][-1] :
		print(student[i][0], student[i][1])


