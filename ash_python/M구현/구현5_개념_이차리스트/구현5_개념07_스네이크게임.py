"""  
	[스네이크게임]
	    1. 10x10 맵이 있다.
	    2. 스네이크는 1234로 표시한다. 머리를 1로 정한다.
	    3. 머리만 상하좌우로 이동이 가능하며, 꼬리가 따라온다.
	    4. 자기몸하고 부딪히면, 사망하여 게임이 종료된다.
	    5. 랜덤으로 아이템(9)를 생성해
	       아이템을 먹으면 꼬리 1개가 자란다.
	    6. 꼬리는 머리포함 최대 8개까지 증가하며, 게임이 종료된다.
		7. 벽을 통과할수없다. 
	     
"""
map = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 3, 4, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]
