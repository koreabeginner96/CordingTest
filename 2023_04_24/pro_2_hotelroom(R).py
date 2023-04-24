def solution(book_time):
    def time(s):
        a,b= map(int,s.split(':'))
        min=a*60+b
        return min
    dict={}
    for i in book_time:
        A=time(i[0])
        B=time(i[1])
        for j in range(A,B+10):
            if not dict.get(j):
                dict[j]=1
            else:
                dict[j]+=1
    return max(dict.values())