def solution(k, score):
    temp=[]
    answer = []
    for i in range(len(score)):
        if i<k:
            temp.append(score[i])
            temp.sort()
            answer.append(temp[0])
        else:
            temp.append(score[i])
            temp.sort()
            temp=temp[-k:]
            answer.append(temp[0])
    return answer