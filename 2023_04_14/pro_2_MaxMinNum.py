def solution(s):
    A=987654321
    B=-987654321
    answer=''
    s=s.split(' ')
    for i in s:
        i=int(i)
        B=max(B,i)
        A=min(A,i)
    A=str(A)
    B=str(B)
    answer+=A
    answer+=' '
    answer+=B
    return answer
print(solution("1 2 3 4"))
