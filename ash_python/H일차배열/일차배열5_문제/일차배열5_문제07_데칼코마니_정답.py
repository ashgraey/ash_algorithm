'''
	[문제]
		a 리스트가 데칼코마니인지 구하시오.
		데칼로마니이면 True를 출력 아니면 False 출력하시오.
		데칼코마니란? 절반으로 나눴을 때 서로 값들이 대칭이면 데칼코마니이다.

	[예시]	
		[1,5,4,4,5,1] True
		[1,5,4,3,5,1] False
'''


a = [1,5,4,4,5,1]

middle = len(a) // 2

count = 0

index = len(a) - 1
for i in range(len(a) // 2):
	if a[i] == a[index]:
		count += 1
	index -= 1

if count == middle:
	print(True)
else:
	print(False)
	