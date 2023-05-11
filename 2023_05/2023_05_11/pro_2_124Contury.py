def solution(n):
    #3진법으로 계산을 하는데 나머지 0일때 4로 변한다음 몫에서-1 해야지 나오는 문제이다.
    #값을 다구한뒤 뒤집어서 연출하면 된다.
    answer = ''
    while n:
        if n % 3:
            #str로 기입을 해야 문제가 더해지지 않는다.
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]

