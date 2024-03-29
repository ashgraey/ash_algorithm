"""
 	[미니마블]
	 
		1. 플레이어는 [p1]과 [p2] 2명이다. 한번씩 번갈아 가면서 행동한다. 
		2. [1.주사위][2.패스] 를 선택할수있다. 주사위는 (1~4)의 랜덤값을 가진다. 
		3. 주사위숫자만큼 현재위치에서 앞으로 이동한다. 
		4. 이동한자리가 다른 플레이어와 같은 위치에 놓이게 되면,
		     상대 플레이어는 잡히게 되어 맨앞(인덱스 0) 으로 강제 이동된다.
		5. 상대를 잡은 위치가 맨앞(인덱스 0)의 위치에 있을때는 안전지대이다.(잡히지않는다.)
		6. 이동거리가 배열의 마지막위치를 초과하면,
			맨앞(인덱스 0)으로 이동하고 초과한숫자만큼 추가이동한다.
		7. 먼저 3바퀴를 돌면 이긴다.
		
		[예시]   
		   [p1] 주사위 : 1
		   1 0 0 0 0 0 0 0 0 0
		   2 0 0 0 0 0 0 0 0 0
		   
		   [p2] 주사위 : 3
		   0 1 0 0 0 0 0 0 0 0
		   0 0 0 2 0 0 0 0 0 0
		   
		   [p1] 주사위 : 2  , [p1]이 [p2]를 잡았다!	   
		   0 0 0 1 0 0 0 0 0 0
		   2 0 0 0 0 0 0 0 0 0 
"""
import random

# 예외처리해야할게 많아서 시간나면 다시 해봐야겠음
class MiniMable : 
    def __init__(self, a, b) :
        self.p1 = a
        self.p2 = b
        self.p1Position = 0
        self.p2Position = 0
        self.win = 0
        self.run()
	
    def turnP1Update(self) :
        print("[1.주사위][2.패스]")
        choice = int(input())
        
        if choice == 1 :
            dice = random.randint(1, 4)
            self.p1Position += dice
        else :
            self.p1Position += 0
    
    def turnP2Update(self) :
        print("[1.주사위][2.패스]")
        choice = int(input())
        
        if choice == 1 :
            dice = random.randint(1, 4)
            self.p1Position += dice
        else :
            self.p1Position += 0
            
    def run(self) :
        self.turnP1Update()
        self.turnP2Update()
        
        while True :
            # 안전지대
            if self.p1Position == 0 and self.p2Position == 0 :
                print(p1)
                print(p2)
            else :
                
# var
p1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
p2 = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
miniMable = MiniMable(p1, p2)