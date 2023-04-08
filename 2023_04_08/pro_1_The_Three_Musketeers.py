from itertools import *
def solution(number):
    answer = 0
    A=0
    answer1=[]
    for i in combinations(number,3):
        answer1.append(i)
    for j in answer1:
        A=0
        for o in j:
            A += o
        if A == 0:
            answer+=1
    return answer
print(solution([-3, -2, -1, 0, 1, 2, 3]))