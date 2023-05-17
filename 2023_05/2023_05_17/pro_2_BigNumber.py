#큰 수를 즉각 비교하여 바로 바로 stack 활용하기
#비교할떄마다 k하나씩 지워주기
#K가 끝까지 남았다면 number[:-K]
#큰 수를 즉각 비교하여 바로 바로 stack 활용하기
#비교할떄마다 k하나씩 지워주기
#K가 끝까지 남았다면 number[:-K]
def solution(number, k):
    stack=[]
    for i in number:
        while stack and stack[-1]<i and k>0:
            stack.pop()
            k-=1
        stack.append(i)
    if k!=0:
        stack=stack[:-k]
    return "".join(stack)
print(solution("1924",2))