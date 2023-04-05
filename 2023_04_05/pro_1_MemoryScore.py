def solution(name, yearning, photo):
    answer = []
    dict={}
    temp=0
    for i in range(len(name)):
        dict[name[i]]=yearning[i]
    for x in photo:
        for j in x:
            if j in dict:
                temp+=dict[j]
        answer.append(temp)
        temp=0
    return answer