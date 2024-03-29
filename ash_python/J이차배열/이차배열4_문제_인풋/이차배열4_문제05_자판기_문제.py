'''
    [문제]
        철수는 편의점에서 아르바이트하고 있다. 
        vending은 음료수 냉장고 물품 개수 상태이다.
        숫자는 아이템 번호이고 
        0은 비어있는 것을 뜻한다.

        냉장고는 최대 10개까지 저장할 수 있다.
        그리고 같은 종류의 아이템으로만 저장하며, 세로로 저장한다.
        box리스트는 현재 아이템 창고 재고를 표시한다.

        왼쪽숫자는 아이템번호이고 오른쪽 숫자는 개수이다.
        예를 들어 [1,4]는 1번 아이템을 뜻하고, 남은개수는 4개를 뜻한다.
        box에 있는 상품들로 채울 수 있을 만큼 채우고 최종상태를 출력하시오.
    [예시]
        1번 아이템은 4개 밖에 재고가 없다.
               
        [vending]
        [0,0,0,0,5,0],
        [0,0,0,0,5,0],
        [1,0,0,0,5,0],
        [1,0,0,0,5,6],
        [1,2,0,0,5,6],
        [1,2,3,0,5,6],
        [1,2,3,0,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6],
        [1,2,3,4,5,6]
    
        [box]
        [1,0],
        [2,8],
        [3,3],
        [4,4],
        [5,8],
        [6,9]
        
        남은 아이템도 채워보자. 
    [정답]     
        [0, 2, 0, 0, 5, 6]
        [0, 2, 0, 0, 5, 6]
        [1, 2, 3, 0, 5, 6]
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]
        [1, 2, 3, 4, 5, 6]

        [1, 0]
        [2, 4]
        [3, 0]
        [4, 0]
        [5, 8]
        [6, 6]
'''
vending = [
    [0,0,0,0,5,0],
    [0,0,0,0,5,0],
    [0,0,0,0,5,0],
    [0,0,0,0,5,6],
    [0,2,0,0,5,6],
    [0,2,3,0,5,6],
    [1,2,3,0,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
]
box = [
    [1,4],
    [2,8],
    [3,3],
    [4,4],
    [5,8],
    [6,9],
]

for i in range(len(box)) :
    count = 0 
    if box[i][0] == 1 :

        j = len(vending) - 1 
        while j >= 0  :
            if vending[j][0] == 0 and count < box[i][1]:
                count += 1
                vending[j][0] = 1
            j -= 1
        box[i][1] -= count
    
    elif box[i][0] == 2 :

        j = len(vending) - 1 
        while j >= 0  :
            if vending[j][1] == 0 and count < box[i][1]:
                count += 1
                vending[j][1] = 2
            j -= 1
        box[i][1] -= count
    
    elif box[i][0] == 3 :

        j = len(vending) - 1 
        while j >= 0  :
            if vending[j][2] == 0 and count < box[i][1]:
                count += 1
                vending[j][2] = 3
            j -= 1
        box[i][1] -= count
    
    elif box[i][0] == 4 :

        j = len(vending) - 1 
        while j >= 0  :
            if vending[j][3] == 0 and count < box[i][1]:
                count += 1
                vending[j][3] = 4
            j -= 1
        box[i][1] -= count
 
    elif box[i][0] == 5 :

        j = len(vending) - 1 
        while j >= 0  :
            if vending[j][4] == 0 and count < box[i][1]:
                count += 1
                vending[j][4] = 5
            j -= 1
        box[i][1] -= count
    
    else :
        j = len(vending) - 1 
        while j >= 0  :
            if vending[j][5] == 0 and count < box[i][1]:
                count += 1
                vending[j][5] = 6
            j -= 1
        box[i][1] -= count

for i in range(len(vending)) :        
    print(vending[i])
print()                
for i in range(len(box)) :        
    print(box[i])