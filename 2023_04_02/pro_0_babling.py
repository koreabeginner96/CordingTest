from itertools import permutations
def solution(babbling):
    cnt=0
    word=[]
    A=["aya", "ye", "woo", "ma"]
    for i in range(1,len(A)+1):
        for j in permutations(A,i):
            word.append(''.join(j))
    for o in babbling:
        if o in word:
            cnt+=1
    return cnt