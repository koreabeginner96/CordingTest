def solution(A:list,B:list):
    answer=0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer+=(A[i]*B[i])
    return answer
