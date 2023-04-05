def solution(n, m, section):
    cnt=paint=0
    for i in section:
        if paint <= i:
            cnt+=1
            paint=i+m
    return cnt
