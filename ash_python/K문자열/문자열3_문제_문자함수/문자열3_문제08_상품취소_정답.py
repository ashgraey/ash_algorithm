'''
    [문제]
        member는 회원목록이다. 번호와 아이디가 기록되어있다.
        item은 쇼핑몰 판매상품이다. 상품이름과 가격이 기록되어있다.
        
        order는 오늘 주문 목록이다. 주문한회원아이디와 아이템이름 그리고, 주문개수가 기록되어있다. 
        cancel은 주문취소 목록이다. 취소한회원아이디와 아이템이름 그리고, 주무개수가 기록되어있다.
        오늘의 매출을 출력하시오.
    [정답]
        7700
'''

member = "qwer1234,pythongood,testid"
item   = "사과,1100/바나나,2000/딸기,4300"
order  = "qwer1234,사과,3/phthongood,바나나,2/qwer1234,딸기,5/testid,사과,4"
cancel = "qwer1234,딸기,5/phthongood,바나나,2"

# member split
memberList = member.split(",")
print(memberList)

# item split
temp = item.split("/")
itemList = []
for i in range(len(temp)):
    info = temp[i].split(",")
    info[1] = int(info[1])
    itemList.append(info)
print(itemList)

# order split
temp = order.split("/")
orderList = []
for i in range(len(temp)):
    info = temp[i].split(",")
    info[2] = int(info[2])
    orderList.append(info)
    print(orderList[i])

# cancel split
temp = cancel.split("/")
cancelList = []
for i in range(len(temp)):
    info = temp[i].split(",")
    info[2] = int(info[2])
    cancelList.append(info)
    print(cancelList[i])

print("------------------------------------------")

# 총 주문내역, 총 취소내역
countList = [0, 0, 0]
for i in range(len(itemList)):
    # 주문 내역
    for j in range(len(orderList)):
        if itemList[i][0] == orderList[j][1]:
            countList[i] += orderList[j][2]
    # 취소 내역
    for j in range(len(cancelList)):
        if itemList[i][0] == cancelList[j][1]:
            countList[i] -= cancelList[j][2]
print(countList)

# 합산
total = 0
for i in range(len(itemList)):
    total += itemList[i][1] * countList[i]
print(total)