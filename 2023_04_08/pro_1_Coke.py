def solution(a:int, b:int, n:int):
    answer = 0
    o=0
    x=0
    while n>=a:
        o= int(n//a)*b
        x= int(n%a)
        answer+=o
        n=x+o
    return answer