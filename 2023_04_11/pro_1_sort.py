def solution(array, commands):
    answer = []
    for i in commands:
        a=array
        a=a[i[0]-1:i[1]]
        a.sort()
        answer.append(a[i[2]-1])
    return answer
