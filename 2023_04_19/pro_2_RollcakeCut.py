#collections 대문자 C 기억하자
from collections import Counter
def solution(topping):
    dict=Counter(topping)
    set_id=set()
    answer = 0
    for i in topping:
        dict[i]-=1
        set_id.add(i)
        if dict[i] == 0:
            dict.pop(i)
        if len(dict)==len(set_id):
            answer+=1
    return answer
