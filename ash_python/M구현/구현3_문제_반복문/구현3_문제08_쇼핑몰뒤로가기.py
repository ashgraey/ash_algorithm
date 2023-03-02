"""
	[쇼핑몰]
		쇼핑몰을 구현하려고한다.
		쇼핑몰의 메인카테고리는 [1.남성의류][2.여성의류][0.종료] 이며,
		남성의류를 선택한경우 [1.티셔츠][2.바지][0.뒤로가기]의 새로운 메뉴가 나온다.
		뒤로가기를 고르기 전까지 세부항목이 계속 보여지게되며, 뒤로가기를 선택하면
		메인카테고리가 다시보여진다.
		세부항목은 아래와 같다.
	[예시]
		1. 남성의류
	 		1. 티셔츠
	 		2. 바지
	 		0. 뒤로가기
	 	2. 여성의류
	 		1. 가디건
	 		2. 치마
	 		0. 뒤로가기
		0. 종료
"""

while True:
    print("[1.남성의류] [2.여성의류] [3.종료]")

    select = int(input())
    if select == 1:
        print("[1.티셔츠] [2.바지] [0.뒤로가기]")
        select = int(input())
        if select == 1:
            print("티셔츠")
            continue
        elif select == 2:
            print("바지")
            continue
        else:
            continue

    elif select == 2:
        print("[1.가디건] [2.치마] [3.뒤로가기]")
        select = int(input())
        if select == 1:
            print("가디건")
            continue
        elif select == 2:
            print("치마")
            continue
        else:
            continue

    elif select == 3:
        break
