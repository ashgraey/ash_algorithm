'''
    [문제]
        lotto리스트가 당첨인지 꽝인지 체크하는 함수를 만드시오.
        단, 7이 연속으로 3개이면 당첨이다.
    [정답]
        당첨
'''
def lottoCk(lotto) :
   
    cnt = 0 
    ck = False
    for i in range(len(lotto)) :
        if lotto[i] == 7 :
            cnt += 1 
            if cnt >= 3 :
                ck = True
                break 
        else : 
            cnt = 0 
    
    result = ""
    if ck == False :
        result = "꽝"
    else :
        result = "당첨"

    return result
 
            
lotto = [1, 7, 7, 1, 7, 7, 7]
a = lottoCk(lotto)
print(a)