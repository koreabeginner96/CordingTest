def solution(numbers:list):
    answer = [-1]*len(numbers)
    stack= []
    for i,e in enumerate(numbers):
        if not stack:
            stack.append((i,e))
            continue
        while stack and stack[-1][1]<e:
            answer[stack[-1][0]]=e
            stack.pop()
        stack.append((i,e))
    return answer
