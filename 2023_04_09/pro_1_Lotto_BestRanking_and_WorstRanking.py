def solution(lottos:list, win_nums):
    answer = []
    cnt=0
    dict={}
    for i in range(7):
        if i<2:
            dict[i]=6
        else:
            dict[i]=7-i
    A=lottos.count(0)
    for i in lottos:
        if i in win_nums:
            cnt+=1
    answer.append(dict[cnt + A])
    answer.append(dict[cnt])
    return answer
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))