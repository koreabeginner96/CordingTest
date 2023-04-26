def solution(storey):
    answer = 0
    while storey:
        r=storey%10
        if r <=4:
            answer+=r
        elif r >=6:
            answer+=(10-r)
            storey+=10
        else:
            if (storey//10)%10<=4:
                answer+=r
            else:
                answer+=r
                storey+=10
        storey=storey//10
    return answer