def time2val(time):
   a,b= map(int,time.split(':'))
   answer= a*60+b
   return answer
def solution(book_time):
    dict={}
    for x,y in book_time:
        x=time2val(x)
        y=time2val(y)+10
        for i in range(x,y):
            if dict.get(i) == None:
                dict[i]=1
            else:
                dict[i]+=1
    return max(dict.values())