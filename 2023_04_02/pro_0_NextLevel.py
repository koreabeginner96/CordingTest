def solution(common):
    if common[1] -common[0] == common[2] -common[1]:
        A=common[1]-common[0]
        Answer=common[0]+A*(len(common))
        return  Answer
    else:
        A=common[1]//common[0]
        Answer=common[0]*(A**len(common))
        return Answer