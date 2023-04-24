def solution(sequence, k):
    answer = []
    sum=0
    L=0
    R=-1
    while True:
        if sum < k:
            R+=1
            if R >= len(sequence):
                break
            sum +=sequence[R]
        else:
            sum-=sequence[L]
            L+=1
            if L >=len(sequence):
                break
        if sum==k:
            answer.append((L,R))
    answer.sort(key=lambda x : (x[1]-x[0],x[0]))
    return answer[0]