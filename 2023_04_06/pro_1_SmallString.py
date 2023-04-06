def solution(t, p):
    answer=0
    A=len(t)
    B=len(p)
    p= int(p)
    for i in range(0,A+1-B):
        if int(t[i:i+B]) <= p:
            answer+=1
    return answer