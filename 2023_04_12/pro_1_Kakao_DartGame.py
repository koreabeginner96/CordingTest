def solution(dartResult):
    answer = 0
    temp=[]
    C=''
    A=[]
    B=['S','D','T']
    for j in range(10):
        A.append(str(j))
    for i in dartResult:
        if i in A:
            C+=i
            continue
        elif i not in A and C != '':
            temp.append(int(C))
            C=''
        if i in B:
            if i == B[0]:
                continue
            elif i == B[1]:
                temp[-1]=temp[-1]**2
            else:
                temp[-1]=temp[-1]**3
        if i == '#':
            temp[-1]=temp[-1]*-1
        if i == '*':
            if len(temp)>=2:
                temp[-2]=temp[-2]*2
                temp[-1]=temp[-1]*2
            else:
                temp[-1]=temp[-1]*2
    for j in temp:
        answer+=j
    return answer
print(solution('1D2S#10S'))