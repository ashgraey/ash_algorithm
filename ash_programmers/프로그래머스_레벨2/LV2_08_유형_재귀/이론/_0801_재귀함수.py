# https://freedeveloper.tistory.com/371

def recursive_function(i):
    # 20번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i== 20:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다')

recursive_function(1)

