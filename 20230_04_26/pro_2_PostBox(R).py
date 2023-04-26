from collections import deque

def solution(order):
    answer=0
    container=[]
    order=deque(order)
    for i in range(1,len(order)+1):
        container.append(i)
        while container and order[0] == container[-1]:
            answer+=1
            order.popleft()
            container.pop()
    return answer