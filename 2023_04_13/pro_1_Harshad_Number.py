def solution(x):
    x=str(x)
    answer=0
    for i in x:
        i=int(i)
        answer+=i
    A=int(x)%answer
    if A ==0:
        return True
    else:
        return False
