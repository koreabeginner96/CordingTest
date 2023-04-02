def solution(A, B):
    answer = 0
    l=len(A)
    while l:
        l -=1
        if A==B:
            return answer
        else:
            answer +=1
            D=A[-1]
            A=D+A[0:len(A)-1]
    if l==0:
        return -1
    return answer