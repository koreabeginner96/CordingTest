def solution(my_str, n):
    temp =[]
    cnt = 0
    answer = []
    for i in my_str:
        temp.append(i)
        cnt += 1
        if n== cnt:
            answer.append(''.join(temp))
            cnt=0
            temp=[]
    if temp:
        answer.append(''.join(temp))
    return answer
