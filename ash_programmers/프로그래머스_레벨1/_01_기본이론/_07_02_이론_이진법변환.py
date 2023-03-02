"""
    [이진법 변환하기] 
        십진법의 수 10을 이진법으로 변환하기.

        이진법의 자리수는 1에 2를 계속 곱한수로 늘어난다.
        
        1,2,4,8,16,32,64 ... 이런식으로 증가한다.

        10을 이진법으로 바꾸기위해서는 10보다는 바로직전에 크거나 같은수 
        즉, 16부터 한칸씩 작은수로 차례대로 나눠주고 나눠진값을 뺀 나머지를 가지고 계속 반복을 하면된다.

        10을 16으로 나눈몫은 0 이고 나머지는 10이된다.
        10을 8 로   나눈몫은 1 이고 나머지는 2가된다.
        2 를 4로    나눈몫은 0 이고 나머지는 2가된다.
        2 를 2로    나눈몫은 1 이고 나머지는 0이된다.
        0 을 1로    나눈몫은 0 이고 나머지는 0이된다. 
        
        위에서 부터 전부 이어붙이면 01010 이되고 맨앞에 0은 제외하면 1010 이되고 이값이 10의 이진법의수이다.
        식으로 표현하면 아래와 같다. 
"""
a = 10
count = 1
while True:
    if count >= a:
        break
    count *= 2
# count 에 2를 계속 곱해주고 10의 값보다 같거나 커지면 종료한다. 
print(count , " " , a)
st = ""
while True:
    st += str(a // count)
    a %= count
    count //= 2
    if count == 0:
        break
print(st)
a = int(st)
print(a)







