def solution(k, tangerine):
    answer = 0
    dict={}
    for i in tangerine:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i]+=1
    dict=sorted(dict.values())
    dict.sort(reverse=True)
    while k>0:
        k-=dict[answer]
        answer+=1
    return answer
print(solution(4,[1, 3, 2, 5, 4, 5, 2, 3]))