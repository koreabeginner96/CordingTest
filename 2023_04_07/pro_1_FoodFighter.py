def solution(food):
    answer =''
    temp=[]
    for i in range(1,len(food)):
        o=food[i]//2
        while int(o)>0:
            o-=1
            temp.extend(str(i))
    for i in range(len(temp)):
        answer+=temp[i]
    return answer+'0'+answer[::-1]
print(solution([1, 7, 1, 2]	))