def solution(number, limit, power):
    answer = 0
    temp1=[]

    for i in range(1,number+1):
        cnt=0
        for j in range(1, int(i ** (1 / 2) + 1)):  # 제곱근까지만 범위 설정
            if i % j == 0:
                cnt += 1
                if j ** 2 != i:  # 제곱이 되는 약수 중복 방지
                    cnt += 1
        temp1.append(cnt)
    for x in temp1:
        if x >limit:
            x=power
        answer+=x
    return answer
print(solution(10,3,2))