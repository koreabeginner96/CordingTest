from itertools import *
def solution(nums):
    cnt=0
    answer=0
    temp1=[]
    temp=[]
    for i in combinations(nums,3):
        temp.append(i)
    for i in temp:
        A=0
        for j in i:
            A+=j
        temp1.append(A)
    temp1.sort()
    for i in temp1:
        for j in range(2,i):
            if i%j==0:
                cnt+=1
        if cnt>=1:
            cnt=0
        else:
            answer+=1
            cnt=0
    return answer
print(solution([1,2,7,6,4]))