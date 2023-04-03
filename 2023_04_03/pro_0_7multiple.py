def solution(array):
    array= str(array)
    answer = 0
    for i in array:
        for j in i[0:]:
            if j=='7':
                answer+=1
    return answer