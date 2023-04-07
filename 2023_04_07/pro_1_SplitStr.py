def solution(s):
    answer = 0
    t=len(s)
    cnt = 0
    cnt1 = 0
    i=0
    c=0
    while t!=c:
        c+=1
        if s[0] == s[i]:
            cnt += 1
            i+=1
        else:
            cnt1 += 1
            i+=1
        if cnt == cnt1:
            answer+=1
            cnt=0
            cnt1=0
            s=s[i:]
            i=0
    if cnt1 or cnt:
        answer+=1
    return answer
