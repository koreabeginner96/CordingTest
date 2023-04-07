from collections import deque
def solution(s:str):
    dict={}
    answer=[]
    for i,d in enumerate((list(s))):
        if d not in dict:
            answer.append(-1)
            dict[d]=i
        else:
            answer.append(i-dict[d])
            dict[d]=i
    return answer
