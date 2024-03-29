"""
    list() 함수는 문자열을 리스트로 만들어준다. 
"""
"""
    map() 함수는 문자로구성되어있는리스트를 정수로 변환해준다. 아래함수와 같이써야한다.
    list(arr)
"""

"""
[문제]
    12345 를 뒤집어서 리스트로 변환하시오. 
[정답]
    [5,4,3,2,1]
"""

n = 12345

arr_n = sorted(str(n), reverse=True)
print(arr_n)

s1 = str(n) # 12345 => "12345"
arr = list(s1) # 문자열을 리스트로 변환 
print(arr) # ['1', '2', '3', '4', '5']

arr.reverse() # 뒤집기

# map을 쓰면 반복문을 안 써도됨
arr = map(int , arr) # 리스트의 값들을 전부 정수로 변환
arr = list(arr) # 변환된 map을 다시 list로 변환 
print(arr)

