def solution(ingredient):
    s=[]
    answer=0
    for i in ingredient:
        s.append(i)
        if s[-4:]==[1,2,3,1]:
            answer+=1
            for j in range(4):
                s.pop()
    return answer