def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in numbers[i+1:]:
            A=numbers[i]+j
            if A not in answer:
                answer.append(A)
    answer.sort()
    return answer
print(solution([5,0,2,7]))