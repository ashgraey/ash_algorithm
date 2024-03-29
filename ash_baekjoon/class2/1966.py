'''
문제
여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 
즉 먼저 요청된 것을 먼저 인쇄한다. 
여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 
하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 
어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

입력
첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

출력
각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.
'''
# 0404 풀어보자
# 조건문에 약해..
import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    size, idx = map(int, input().split())
    arr = deque(map(int, input().split()))
    idxList = deque([*range(size)]) # 인덱스 리스트를 따로 만들어야 하는게 point
    # print(idxList)

    cnt = 0 
    # arr에 값이 있을 때까지 반복문을 돌림
    while arr :
        if arr[0] == max(arr) :
            arr.popleft() # max값이 나올때마다 하나씩 제거, max의 값은 계속 바뀜
            cnt += 1
            if idxList.popleft() == idx :
                print(cnt)
                break
        
        else :
            arr.append(arr.popleft())
            idxList.append(idxList.popleft())

# 인터넷 정답// 어렵다 다시 풀어야겠다
# import sys
# from collections import deque
# input = sys.stdin.readline

# tc = int(input())
# for _ in range(tc):
#     n, m = map(int, input().split())
#     que = deque(list(map(int, input().split())))    # 중요도
#     idx = deque(list(range(n)))                     # 인덱스
#     print(idx)
   
#     cnt = 0
#     while que:
#         if que[0] == max(que):      # 첫번째 요소가 최댓값이면
#             cnt += 1                # 카운트
#             que.popleft()           # pop
#             if idx.popleft() == m:  # 인덱스가 m과 같을 때
#                 print(cnt)          # 카운트 값 출력
#         else:
#             que.append(que.popleft())   # 왼쪽 값 pop해 append
#             idx.append(idx.popleft())
        
#         print(que)
#         print(idx)

# 중요도가 가장 높은 순서전의 인덱스는 큐의 뒤로 차례대로 보낸뒤 
# 중요도가 높은 순으로 출력한다.
# 3번째 케이스를 어케해야할지..
# from collections import deque 
# import sys
# input = sys.stdin.readline

# case = int(input())
# # for _ in range(case) :
# #     size, idx = map(int, input().split())
# #     pList = [*map(int, input().split())]
# #     # print(pList)
# size, idx = map(int, input().split())
# pList = deque([*map(int, input().split())])


# max = max(pList)
# # pList.pop(max)
# print(pList)
# print(max)



# slicing = deque(pList[:maxIdx])
# slicing.appendleft(pList[maxIdx])
# print(slicing)
# print(pList)
# print(case, size, idx, pList)
