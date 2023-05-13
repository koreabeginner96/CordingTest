#전형적인 DP 문제이다. 점화식이라고 TOP-Bottom 숫자를 줄여 가면서 푸는 문제이다.
def solution(n):
    answer=0
    while n>0:
        if n%2 ==0:
            n=n//2
        else:
            answer+=1
            n=(n-1)//2
    return answer
