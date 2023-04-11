def solution(N, stages:list):
    answer = []
    D=[]
    temp=[]
    stages.sort()
    for i in range(1,N+1):
        B=0
        for j in stages:
            A=len(stages)
            if i>=j:
                B+=1
        temp.append(float(B/A))
        stages=stages[B:]
    answer.extend(temp)
    temp.sort(reverse=True)
    for i in temp:
        if i in answer:
            A=answer.index(i)
            D.append(A+1)
            answer[A]=' '
    return D