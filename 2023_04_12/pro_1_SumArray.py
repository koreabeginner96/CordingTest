def solution(arr1, arr2):
    answer = []
    temp=[]
    for x,y in zip(arr1,arr2):
        for i in range(len(x)):
            temp.append(x[i]+y[i])
        answer.append(temp)
        temp=[]
    return answer
print(solution([[1,2],[2,3]],[[3,4],[5,6]]))