def solution(data, col, row_begin, row_end):
    answer = 0
    #동일 값 일경우 data 기준으로 내림차순 -x[0]을 기억해야한다.
    d=sorted(data,key=lambda x : (x[col-1],-x[0]))
    for i in range(row_begin,row_end+1):
        result=0
        #나머지들의 합
        for j in d[i-1]:
            result += (j % i)
            # bitwise xor 연산자 ^=
        answer ^= result
    return answer
