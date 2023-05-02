def solution(numbers):
    numbers=list(map(str,numbers))
    numbers.sort(key=lambda x : x*3 ,reverse=True)
    return str(int(''.join(numbers)))
'''합치기위해 list(map(str,numbers) 바꾼다.
sort lambda 함수를 하고 x*3을 하는 이유는 아스키 코드로 작업을 하기 떄문이다.
마지막 str int 로 바꾸는 이유는 000을 제거 하기 위해서 이다.'''