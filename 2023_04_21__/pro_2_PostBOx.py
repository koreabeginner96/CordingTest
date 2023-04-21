from collections import deque
def solution(order):
    answer = 1
    l=len(order)
    stack=deque()
    order=deque(order)
    p=deque()
    x=order.popleft()
    for i in range(x+1,l+1):
        p.append(i)
    for i in range(1,x):
        A=x-i
        stack.append(A)
    for j in order:
        if j == stack[0]:
            answer += 1
            stack.popleft()
        elif j >= p[0]:
            A=j-p[0]
            p.remove(p[0:A])
            stack.insert(0,p[0:A])
        elif j == p[0]:
            answer += 1
        else:
            return answer
    return answer
print(solution([5, 4, 3, 2, 1]))