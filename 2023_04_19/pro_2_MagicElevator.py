def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        # 5
        #3-1. 만약 다음 자릿값이 5 ~ 9에 해당한다면 현재 자릿값을 10 에 도달하는 방향으로 마법의 돌을 사용한다.
        #3-2. 만약 다음 자릿값이 0 ~ 4에 해당한다면 현재 자릿값을 0 에 도달하는 방향으로 마법의 돌을 사용한다.
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10

    return answer
print(solution(2554))