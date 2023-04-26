from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    cnt=0
    A = sum(queue1)
    B = sum(queue2)
    if (A+B)%2 !=0:
        return -1
    for i in range(len(queue1)*4):
        if A==B:
            return cnt
        while A>B:
            o=queue1.popleft()
            queue2.append(o)
            A-=o
            B+=o
            cnt+=1
        while A<B:
            o=queue2.popleft()
            queue1.append(o)
            cnt+=1
            A+=o
            B-=o
    return -1