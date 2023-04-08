def solution(survey, choices):
    answer = ''
    N=['R','T','C','F','J','M','A','N']
    dict = {}
    dict1= {}
    temp=[]

    s = 4
    for i in range(1, 8):
        if i > 4:
            s += 1
        elif i == 4:
            s = 0
        else:
            s -= 1
        dict[i] = s
    for j in range(len(survey)):
        if choices[j] <4:
            temp.append((survey[j][0],dict[choices[j]]))
        elif choices[j] ==4:
            continue
        else:
            temp.append((survey[j][1], dict[choices[j]]))
    for x,y in temp:
        if x not in dict1:
            dict1[x]=y
        else:
            dict1[x]=dict1[x]+y
    for i in N:
        if i not in dict1:
            dict1[i]=0
    for o in range(0,8,2):
        A=N[o]
        N[o]=dict1[N[o]]
        B=N[o+1]
        N[o+1]=dict1[N[o+1]]
        if N[o]<N[o+1]:
            answer+=B
        else:
            answer+=A
    return answer
print(solution(["TR", "RT", "TR"],[7, 1, 3]))
