from collections import deque

def bfs(o,start,end,n):
    que=deque()
    que.append(start)
    while que:
        x=que.popleft()
        if x == end:
            return o[end]-1
        for i in range(3):
            if i==0:
                nx=  x*2
            elif i==1:
                nx= x*3
            else :
                nx = x+n
            if nx <= end:
                #2
                if o[nx] ==1:
                    que.append(nx)
                    o[nx]=o[x]+1
def solution(x, y, n):
    if x==y:
        return 0
    #1
    o=[1 for _ in range(y+1)]
    #3
    cnt=bfs(o,x,y,n)
    if cnt:
        return cnt
    else:
        return -1
