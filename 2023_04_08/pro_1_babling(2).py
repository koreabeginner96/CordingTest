def solution(babbling):
    answer = 0
    A=["aya", "ye", "woo", "ma"]
    for i in babbling:
        for p in A:
            if p*2 not in i:
                i=i.replace(p,' ')
       #if i.strip() == '':
        if i.ispace() :
            answer+=1
    return answer