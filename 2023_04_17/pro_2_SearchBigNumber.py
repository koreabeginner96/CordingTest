from collections import deque
def solution(numbers):
    answer=[-1]*len(numbers)
    stack=deque()
    for i,e in enumerate(numbers):
        if not stack:
            stack.append((i,e))
            continue
        while stack and stack[-1][1] < e :
            si,se =stack.pop()
            answer[si]=e
        stack.append((i,e))
    return answer
print(solution([2, 3, 3, 5]))