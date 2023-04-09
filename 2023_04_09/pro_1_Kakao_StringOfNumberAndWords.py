def solution(s:str):
    A=['zero','one','two','three','four','five','six','seven','eight','nine']
    dict={}
    for i in range(10):
        dict[A[i]] = i
    for j in dict:
        if j in s:
            s=s.replace(str(j),str(dict[j]))
    return int(s)
